from logging import PlaceHolder
import math
from multiprocessing import Value
from itertools import combinations
import pylab as pl
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import numpy as np
import numpy.random as random
from  numpy.core.fromnumeric import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math as m
import plotly.figure_factory as ff
from collections import Counter
import streamlit as st

def app(Data):
    st.title("Assignment 8")
    def printf(url):
         st.markdown(f'<p style="color:#000;font:lucida;font-size:25px;">{url}</p>', unsafe_allow_html=True)
    operation = st.selectbox("Operation", ["Crawler_bfs","Crawler_dfs","Page_Rank_Algo"])
    if operation == "Crawler_bfs":
        vis = dict()
        sst = set()
        q = []
        def bfs():
            while(len(q)>0):
                nxt_url = q[0] 
                q.pop(0)
                try:
                    st.write("*************************level: ",vis[nxt_url],"*******************************")
                    # if(vis[link.get('href')])>6:
                        # return 
                except KeyError:
                    pass
                try:
                    req = Request(nxt_url)
                    html_page = urlopen(req)
                    soup = BeautifulSoup(html_page, "lxml")
                except Exception:
                    pass
                cnt = 0 ;
                for link in soup.findAll('a'):
                    st.write(link.get('href'))
                    # if(vis[link.get('href')]==0):
                    if(link.get('href') not in sst):
                        q.append(link.get('href'))
                        sst.add(link.get('href'))
                    try:
                        vis[link.get('href')] = vis[nxt_url] + 1
                        if(vis[link.get('href')])>5:
                            return  
                    except KeyError:
                        pass
                    cnt = cnt + 1 ;
                    if(cnt>20):
                        break 
            
                # for link in links:
                    # print(link) 
                if(len(sst)>10000):
                    return 

        seed_url = "http://google.com"
        # req = Request("http://google.com")
        # html_page = urlopen(req)

        # soup = BeautifulSoup(html_page, "lxml")

        # links = []
        # for link in soup.findAll('a'):
        #     links.append(link.get('href'))
        vis[seed_url] = 0  
        q.append(seed_url)
        bfs()

        # for link in st: 
            # print(link)
        # for link in links:
        #     print(link)
    if operation == "Crawler_dfs":
        q = []
        # vis = dict()
        sst = set()
        def dfs():
            while(len(q)>0):
                nxt_url = q[-1] 
                q.pop(-1)
                try:
                    req = Request(nxt_url)
                    html_page = urlopen(req)

                    soup = BeautifulSoup(html_page, "lxml")
                except Exception:
                    pass
                cnt = 0 ;
                for link in soup.findAll('a'):
                    if(link is not None):
                        st.write(link.get('href'))
                    # if(vis[link.get('href')]==0):
                    if(link.get('href') not in sst):
                        q.append(link.get('href'))
                        sst.add(link.get('href'))
                    try:
                        pass
                        # vis[link.get('href')] = vis[nxt_url] + 1
                        # if(vis[link.get('href')])>5:
                            # return  
                    except KeyError:
                        pass
                    cnt = cnt + 1 ;
                    if(cnt>20):
                        break 
            
                # for link in links:
                    # print(link) 
                if(len(sst)>10000):
                    return 

        seed_url = "http://google.com"
        # req = Request("http://google.com")
        # html_page = urlopen(req)

        # soup = BeautifulSoup(html_page, "lxml")

        # links = []
        # for link in soup.findAll('a'):
        #     links.append(link.get('href'))
        # vis[seed_url] = 0  
        q.append(seed_url)
        dfs()

        # for link in st: 
            # print(link)
        # for link in links:
        #     print(link)

    if operation == "Page_Rank_Algo":
        file = open("C:\\Users\\Akash\\Downloads\\data mining\\Assignment8\\stnfordgraph.txt", "r")
        flg = 0 ;
        content = file.readlines()

        adj_mat = {}
        for line in content:
            # print(line)
            if(flg==0):
                lin = line.split(' ')
                vertex = int(lin[0])
                edges = int(lin[1][:])
                # print(edges)
                flg = 1
                adj_mat = {new_list: [] for new_list in range(vertex+1)}
                in_deg = [0]*(vertex+1)
                out_deg = [0]*(vertex+1)
            else:
                lin = line.split(' ')
                tmp = lin[0].split('\t')
                # print(tmp)  
                adj_mat[int(tmp[1][:-1])].append(int(tmp[0]))
                in_deg[int(tmp[1][:-1])] += 1
                out_deg[int(tmp[0])] += 1
        file = open('geek.txt','w')
        # print(out_deg)
        def calclute_pagerank():
            cnt = 0
            itr = 1
            while(cnt<=vertex+1):
                file.write(str("******Iteration" +str(itr)+" ******"))
                for i in range(1,vertex+1):
                    tmp_prnk[i] = 0 ;
                    for no in adj_mat[i]:
                        tmp_prnk[i] += (page_Rank[no]/out_deg[no])
                    if((abs(tmp_prnk[i]-page_Rank[i])/(page_Rank[i]))*100<=0.0001):
                        cnt += 1
                    if(tmp_prnk[i]):
                        page_Rank[i] = tmp_prnk[i]
                    file.write(str(page_Rank[i])+" ")
                itr+=1 
            return itr ;
        page_Rank = [1/(vertex)]*(vertex+1)
        tmp_prnk = [0]*(vertex+1) 
        page_Rank[0] = 0
        # out_deg = [0,2,0,3,2,2,1]
        # file.write(str(page_Rank))
        itr = calclute_pagerank()
        index = {}
        st.write("Number of iteration is : ", itr)
        for i in range(1,vertex+1):
            index[page_Rank[i]] = i ;
        page_Rank.sort()
        for i in range(1,11):
            st.write("Top ",i, "web page number is ", index[page_Rank[-i]] , "page rank is ",page_Rank[-i]);
                # st.write("Web and their Page rank")
                # for i in range(1,vertex+1):
                    # st.write(i," page their ",page_Rank[-i])
    if operation == "HITS":
        input_list = []
        
        st.subheader("Dataset")
        st.dataframe(Data.head(1000), width=1000, height=500)
        vertex = set()
        for i in range(len(Data)):
                input_list.append([Data.loc[i, 'fromNode'],Data.loc[i, 'toNode']])
                vertex.add(Data.loc[i, 'fromNode'])
                vertex.add(Data.loc[i, 'toNode'])
        size = len(vertex)
        adj_matrix = np.zeros([size+1,size+1])

        for i in input_list:
            adj_matrix[i[0]][i[1]] = 1
        
        printf("No of Nodes: "+str(size))
        printf("No of Edges: "+str(len(Data)))
        st.subheader("Adjecency Matrix")
        st.dataframe(adj_matrix, width=1000, height=500)
        A = adj_matrix
        # st.dataframe(A)
        At = adj_matrix.transpose()
        st.subheader("Transpose of Adj matrix")
        st.dataframe(At)

        u = [1 for i in range(size+1)]
        printf("Hub weight matrix (U)")
        st.dataframe(u)
        # printf("Hub weight vector (V)")
        # printf(u)
        v = np.matrix([])
        for i in range(5):
            v = np.dot(At,u)
            u = np.dot(A,v)

        # u.sort(reverse=True)
        hubdict = dict()
        for i in range(len(u)):
            hubdict[i]= u[i]
        
        authdict = dict()
        for i in range(len(v)):
            authdict[i]=v[i]

        hubdict = dict( sorted(hubdict.items(), key=operator.itemgetter(1),reverse=True))
        authdict = dict( sorted(authdict.items(), key=operator.itemgetter(1),reverse=True))
        # printf(sorted_rank)
        printf("HubPages : ")
        i = 1
        printf(f"Rank ___ Node ________ Hubs score")
        for key, rank in hubdict.items():
            if i == 11:
                break
            printf(f"{i} _____ {key} ________ {rank}")
            i += 1

        printf("Authoritative Pages : ")
        i = 1
        printf(f"Rank ___ Node ________ Auth score")
        for key, rank in authdict.items():
            if i == 11:
                break
            printf(f"{i} _____ {key} ________ {rank}")
            i += 1





        