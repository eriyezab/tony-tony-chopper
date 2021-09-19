import requests
from bs4 import BeautifulSoup

from typing import List
from typing import Any

LIBGEN_LINK = "http://libgen.rs/"
QUERY_PREFIX = "search.php?req="
QUERY_SUFFIX = "&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
TABLE_COLS = [
        "ID",
        "Authors",
        "Title",
        "Publisher",
        "Year",
        "Pages",
        "Language",
        "Size",
        "Extension",
        "Mirror 1",
        "Mirror 2",
        "Mirror 3",
        "Mirror 4",
        "Mirror 5",
        "Edit",
        ]


class Libgen:
    """
    Responsible for searching libgen for download links to different forms
    of text.
    """

    def search(
            self, 
            book: str,
            author: str = "",
            file_formats: List[str] = [], 
            max_file_size_mb: int = 100,
            language: str = "English",
            year: int = 0,
            pages: int = 0
            ) -> bool:
        """
        Returns a list of download links for the given book.
        """
        if not book:
            return False

        query = '+'.join(book.split(' '))
        page = requests.get(LIBGEN_LINK + QUERY_PREFIX + query + QUERY_SUFFIX)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.findChildren("table")[2]
        
        self.__filter_table(
                table,
                author,
                file_formats,
                max_file_size_mb,
                language,
                year,
                pages
                )
        # print(soup.prettify())
        return True

    def __filter_table(
            self,
            table, 
            author: str,
            file_formats: List[str], 
            max_file_size_mb: int,
            language: str,
            year: int,
            pages: int
            ) -> List[Any]:
        rows = table.findChildren("tr")

        filtered_rows = []
        i = 0
        for row in rows[1:]:
            cells = row.findChildren("td")
            valid = True
            for cell in cells:
                print(cell)
            break
        return filtered_rows
        
