# README
This was a quick demo of how pass by value works with references. It follows a popular discussion on a StackOverflow [post](https://stackoverflow.com/questions/40480/is-java-pass-by-reference-or-pass-by-value).

This was my first intro to using manim and since there's a lack of documentation it was a little challenging. More importantly this was one of the few times creating something through more of a trial and error process instead of following tutorials or reading documentation (could find very simple ones at the time). Feel free to reach out to mention your own forms of developing something without proper resources as I'm sure my way is likely naive.

## Challenges
1. Knowing what to do
  Luckily 3Blue1Brown has tons of examples since we posts his code to the repo. Using his videos find the part of code that represents it. For me I used his cryptocurrency video to understand how to use VGroups. If I couldn't find I would take a stab in the dark and use searching tools like ack or ag to find keywords. 
2. How to organize 
  I don't think my structure is the best but had I taken the time to draw things out the organization of the code would have naturally followed. Unfortunately I didn't do this and ended up editing the code constantly to make changes. 
3. How to place shapes around
  a. This was done through moving individual shapes around using next_to,move_to, and similar functions
  ```python
  ...
  # moves var_name object below the block object
  var_name.next_to(block,DOWN)
  ...
  # move updated_pointer_address object exactly where the last blocks object is
  updated_pointer_address.move_to(self.blocks[-1])
  ```
  b. The alternative was to use VGroup to bundle things together.
    The following code will create a group starting from the first own then moving DOWN like so
    
    block1 
              buff
    block2
              buff    
    ...
              buff       
    blockn
    
  ```python
  ...
  blocks = VGroup()
  blocks.arrange(DOWN, buff = 1.5)
  # move the group the LEFT edge of the screen
  blocks.to_edge(LEFT)
  ```
