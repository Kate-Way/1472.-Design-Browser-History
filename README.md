# 1472.-Design-Browser-History

The best way to design browser history is to use a doubly linked list, so you have a track of every next and previous nodes.
Once you introduce a new node (new url) it becomes your next node and the link to the previous forward history is automatically broken. You don't need to delete anything, you just write new data. 
Here is an example: let's say you've visited following websites: Google (your homepage) -> Twitter -> LinkedIn -> Leetcode
Then you went back two steps: and now you're back at Twitter
Then from Twitter (your curr page) you've decided to visit YouTube. YouTube becomes curr.next, Twitter becomes curr.previous for YouTube. There are no longer links to LinkedIn and Leetcode. They are gone as soon as you've decided to go to new address instead of following 'next' path. 
