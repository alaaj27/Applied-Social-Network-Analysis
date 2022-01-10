
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 2 - Network Connectivity
# 
# In this assignment you will go through the process of importing and analyzing an internal email communication network between employees of a mid-sized manufacturing company. 
# Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

# In[1]:


import networkx as nx

# This line must be commented out when submitting to the autograder
#!head email_network.txt


# ### Question 1
# 
# Using networkx, load up the directed multigraph from `email_network.txt`. Make sure the node names are strings.
# 
# *This function should return a directed multigraph networkx graph.*

# In[2]:


def answer_one():
    
    # Your Code Here
    
    G = nx.read_edgelist(path='email_network.txt', data=[('time', int)], create_using=nx.MultiDiGraph())
    return G # Your Answer Here


# ### Question 2
# 
# How many employees and emails are represented in the graph from Question 1?
# 
# *This function should return a tuple (#employees, #emails).*

# In[3]:


def answer_two():
        
    G = answer_one()
    
    return len(G.nodes()), len(G.edges())


# ### Question 3
# 
# * Part 1. Assume that information in this company can only be exchanged through email.
# 
#     When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# *This function should return a tuple of bools (part1, part2).*

# In[4]:


def answer_three():
        
   
    G = answer_one()
    S = nx.is_strongly_connected(G) 
    W = nx.is_weakly_connected(G)
    return S, W # Your Answer Here


# ### Question 4
# 
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# 
# *This function should return an int.*

# In[5]:


def answer_four():
        
    G = answer_one()
    Weakly_connected_comonents = nx.weakly_connected_components(G)
    Max_WCC = max(Weakly_connected_comonents, key=len)
    return len(Max_WCC)


# ### Question 5
# 
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# 
# *This function should return an int*

# In[6]:


def answer_five():
    G = answer_one()
    Strongly_connected_components = nx.strongly_connected_components(G)
    Max_SCC = max(Strongly_connected_components, key=len)
    return len(Max_SCC)


# ### Question 6
# 
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. 
# Call this graph G_sc.
# 
# *This function should return a networkx MultiDiGraph named G_sc.*

# In[7]:


def answer_six():
    
    G = answer_one()
    Strongly_connected_components = nx.strongly_connected_component_subgraphs(G)
    G_sc = max(Strongly_connected_components, key=len)
    return G_sc


# ### Question 7
# 
# What is the average distance between nodes in G_sc?
# 
# *This function should return a float.*

# In[11]:


def answer_seven():
        
    # Your Code Here
    G_sc = answer_six()
    Shortest_path = nx.average_shortest_path_length(G_sc)
    return Shortest_path # Your Answer Here


# ### Question 8
# 
# What is the largest possible distance between two employees in G_sc?
# 
# *This function should return an int.*

# In[12]:


def answer_eight():
        
    # Your Code Here
    G_sc = answer_six()
    d = nx.diameter(G_sc)
    return d# Your Answer Here


# ### Question 9
# 
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# 
# *This function should return a set of the node(s).*

# In[13]:


def answer_nine():
       
    G_sc = answer_six()
    setOfNodes = set(nx.periphery(G_sc))
    return setOfNodes


# ### Question 10
# 
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# 
# *This function should return a set of the node(s).*

# In[16]:


def answer_ten():
        
    # Your Code Here
    G_sc = answer_six()
    setOfNodes = set(nx.center(G_sc))
    return setOfNodes
    


# ### Question 11
# 
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# 
# How many nodes are connected to this node?
# 
# 
# *This function should return a tuple (name of node, number of satisfied connected nodes).*

# In[22]:


def answer_eleven():
        
    G_sc = answer_six()    
    periphery = nx.periphery(G_sc)
    diameter = nx.diameter(G_sc)
    target_Node=None
    maximum=-1
    
    for node in periphery:
        count = 0
        for k, val in nx.shortest_path_length(G_sc, node).items():
            if val == diameter:
                count = count+ 1
                
        if count > maximum:
            target_Node = node
            maximum = count    
    
    return target_Node, maximum   


# ### Question 12
# 
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)? 
# 
# *This function should return an integer.*

# In[23]:


def answer_twelve():
        
    G = answer_six()
    c, n = nx.center(G)[0], answer_eleven()[0]
    count= len(nx.minimum_node_cut(G, c, n))
    return  count


# ### Question 13
# 
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# 
# *This function should return a networkx Graph.*

# In[19]:


def answer_thirteen():
        
    G = answer_six()
    return nx.Graph(G.to_undirected())  # Your Answer Here


# ### Question 14
# 
# What is the transitivity and average clustering coefficient of graph G_un?
# 
# *This function should return a tuple (transitivity, avg clustering).*

# In[26]:


def answer_fourteen():
        
    G = answer_thirteen()
    tran = nx.transitivity(G)
    clus = nx.average_clustering(G)
    return tran, clus   # Your Answer Here

