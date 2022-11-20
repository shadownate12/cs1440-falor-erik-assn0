**Software Development Plan**  
System Requirements: Create a program to accept one or two command line arguments:  
1) Starting URL specified as an absolute URL.  
2) [Optional] the maximum distance in number of links from the starting website to navigate.   (default 3).

Crawl() must take the following parameters: 
1) url: an absolute URL
2) depth: current depth of recursion
3) maxdepth: max distance of recursion
4) visited: a set of URLs that have been visited  

**Do not return anything from Crawl()**.  
Start by supplying a depth of zero. Set an empty set for visited.  
**When Crawl is called:**  
If depth exceeds maxDepth, return.  
Fetch webpage url. Report exceptions when an unreachable url is encountered.  
Scan for <a>. If href is encountered check for http and https. Otherwise, discard.  
If not an absolute URL, add https:// using urljoin().  
Check if in visited. If so, loop to next anchor tag. If not, record into visited. Print out URL, indicate current depth using indentation. call Crawl().
