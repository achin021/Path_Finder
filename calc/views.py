from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Achin'})

def add(request):
    val1 = (request.GET['num1'])
    val2= (request.GET['num2'])
    
    graph = {'a':{'b':0.5,'j':0.6,'m':1,'n':0.6,'p':0.5},'b':{'c':0.8,'d':0.7,'j':0.7,'a':0.5},'c':{'u':0.4,'v':0.6,'d':0.3,'j':1.0,'b':0.8},'d':{'c':0.3,'u':0.5,'v':0.5,'j':0.9,'b':0.7},'e':{'j':1.5,'v':1.2,'t':1.1,'k':2.6},'j':{'d':0.9,'e':1.5,'m':1.9,'a':0.6,'c':1,'b':0.7},'k':{'e':2.6,'lh':0.6,'m':0.7},'lh':{'k':0.6},'m':{'n':0.7,'a':1.0,'j':1.9,'k':0.7},'n':{'p':0.4,'a':0.6,'m':0.7},'p':{'q':0.6,'n':0.4,'a':0.5},'q':{'p':0.6},'u':{'c':0.4,'d':0.5,'v':0.2,'t':0.4},'v':{'c':0.6,'u':0.2,'t':0.6,'e':1.2,'d':0.5},'t':{'u':0.4,'v':0.6,'e':1.1}}                                                                                          
    shortest_distance = {}
    path = []
    def dijkstra(graph,start,goal):
        
        predecessor = {}
        unseenNodes = graph
        infinity = 999999
        
        for node in unseenNodes:
            shortest_distance[node] = infinity
        shortest_distance[start] = 0
    
        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
    
            for childNode, weight in graph[minNode].items():
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.pop(minNode)
    
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Path not reachable')
                break
        path.insert(0,start)
        
    
    
    dijkstra(graph, val1, val2)

 









    
    return render(request, "result.html", {'path':path , 'distances':round(shortest_distance[val2],1), 'cost':round(shortest_distance[val2]*5,1)})
    