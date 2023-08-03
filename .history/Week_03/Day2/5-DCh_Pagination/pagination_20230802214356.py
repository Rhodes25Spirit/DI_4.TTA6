import math

alphabetlist = "abcdefghijklmnopqrstuvwxyz"

alphabetlist = [*alphabetlist]

Pagination_size = 4

the_current_page_is = 0


class Pagination:
    def __init__(self, alphabetlist, Pagination_size):
        self.alphabetlist = alphabetlist
        self.Pagination_size = Pagination_size
        self.totalPages = math.ceil(len(alphabetlist) / Pagination_size) - 1
        self.currentPage = 0

    def getVisibleItems(self):
        return self.alphabetlist[
            self.Pagination_size
            * self.currentPage : (
                self.Pagination_size * (self.currentPage) + self.Pagination_size
            )
        ]

    def nextPage(self):
        if self.currentPage > self.totalPages - 1:
            return print("You are on the last page")
        else:
            self.currentPage += 1
            return self.getVisibleItems()

    def prevPage(self):
        if self.currentPage <= 1:
            return print("You are on the first page")
        else:
            self.currentPage -= 1
            print(self.getVisibleItems())

    def firstPage(self):
        self.currentPage = 0
        print(self.currentPage)
        self.getVisibleItems()

    def lastPage(self):
        self.currentPage = self.totalPages
        self.getVisibleItems()

    def goToPage(self, pageNum):
        self.currentPage = pageNum
        return self.alphabetlist[
            self.Pagination_size
            * self.currentPage : (
                self.Pagination_size * (self.currentPage) + self.Pagination_size
            )
        ]


page1 = Pagination(alphabetlist, Pagination_size)


print(page1.getVisibleItems())
print(page1.nextPage())
print(page1.nextPage())
print(page1.nextPage())
print(page1.nextPage())
print(page1.prevPage())
print(page1.nextPage())
print(page1.nextPage())
print(page1.nextPage())
print(page1.nextPage())


print(page1.goToPage(1))