
stack = []
dfn = [-1 for x in xrange(5)]
low = [-1 for x in xrange(5)]
cnt = 0


graph = [[1,2],[],[1,3],[4],[2]] #adjacent list

def dfs(u):
    global stack
    global dfn
    global cnt
    dfn[u]=low[u]=cnt
    cnt += 1
    stack.append(u)

    for v in graph[u]:
        if dfn[v]==-1:
            dfs(v)
            low[u]=min(low[u],low[v])
        else:
            low[u]=min(low[u],dfn[v])
    #print "%d->%d"%(u,low[u])
    if low[u]==dfn[u]:
        print 'new scc'
        while True:
            print stack[-1]
            v = stack[-1]
            dfn[v]=5
            if stack[-1] == u:
                del stack[-1]
                break
            del stack[-1]
    

def tarjan():
    for u in xrange(len(graph)):
        if dfn[u]==-1:
            dfs(u)

tarjan()

