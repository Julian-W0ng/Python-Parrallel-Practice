import concurrent.futures
import wikipediaapi
import dill
from pathos.multiprocessing import ProcessingPool


class PathFinder:
    __wiki = wikipediaapi.Wikipedia('en')

    @staticmethod
    def __build_layer(page) -> dict:
        paths = dict()
        print(page.title)
        for p in page.links:
            paths[p] = [page.title, p]
        return paths

    @staticmethod
    def __search_layer(page, target) -> list:
        path = [page.title]
        if page.title == target.title:
            return path
        else:
            if target.title in page.links:
                path.append(target.title)
                return path
            else:
                pool = ProcessingPool()
                pages = list(pool.map(PathFinder.__wiki.page, page.links))
                paths = pool.map(PathFinder.__build_layer, pages)
                valid = dict()
                for p in paths:
                    valid.update(p)
                path.extend(valid[target.title])
                return path


    @staticmethod
    def find_path(start, end) -> list:
        page = PathFinder.__wiki.page(start)
        target = PathFinder.__wiki.page(end)
        if not (page.exists() and target.exists()):
            raise ValueError('Page or Target Does Not Exist')
        else:
            return PathFinder.__search_layer(page, target)


