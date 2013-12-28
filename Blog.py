class Post:
    def __init__(self,content,author):
        self.content = content
        self.author = author
    def __repr__(self):
        return '<'+self.author+'>'+self.content
    def __lt__(self,other):
        return self.author < other.author
    
class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self,post):
        self.posts.append(post)
    def __repr__(self):
        s=""
        for post in self.posts:
            s += str(post)+'\n'
        return s.rstrip()
    def sort(self):
        self.posts.sort()

p1=Post("Horse","Ma")
p2=Post("Dog","Liu")
p3=Post("Chicken","Ning")
blog = Blog()
blog.add_post(p1)
blog.add_post(p2)
blog.add_post(p3)
print blog
print '-----------'
blog.sort()
print blog
