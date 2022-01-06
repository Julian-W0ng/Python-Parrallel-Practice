import concurrent.futures


def find_path(page, target, wiki) -> list:
    start = wiki.page(page)
    end = wiki.page(target)
    if not start.exists() and not end.exists():
        raise ValueError('Page or Target Does Not Exist')
    else:
        return search_site(start, end, wiki)


is_page = lambda page, target: page.title == target.title


def search_site(page, target, wiki) -> list:
    path = [page]
    if is_page(page, target):
        return path
    else:
        executor = concurrent.futures.ProcessPoolExecutor()
        valid_pages = list()
        executor.map(print, page.links)
        executor.map(lambda p: valid_pages.append(p) if is_page(p, target) else False, page.links)
        if len(valid_pages) > 0:
            path.append(valid_pages[0])
            return path
        else:
            raise ValueError('Not Found')

