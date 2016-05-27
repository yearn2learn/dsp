# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, [practice](http://www.keybr.com/) until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.

---

### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.



---

###Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

###Q1. Terminal Editor

What terminal editor will you use? How did you make your decision?

  I will be using Emacs since it seems to be more efficient than Vim since you don't have to keep switching modes and enables the user to easily do so much more. This [online thread](http://unix.stackexchange.com/questions/986/what-are-the-pros-and-cons-of-vim-and-emacs) helped me decide by laying out the differences in usability and features.


--

###Q2. Graphical Editor

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

  I have been using Sublime a lot in the past, however, I want to try using Atom as it is relatively similar to Sublime as well as open source. Some great features of Atom are auto-completion, multiple panes, markdown preview, lots of cool packages including the ability to use terminal inside the editor (using terminal-plus package). Using such packages enables you to customize it exactly to your liking.

Shortcuts:  
Ctrl - p          -> Opens the Fuzzy Finder palette in which you can search and open files

Ctrl - Shift - m	 -> Previews the file in the Markdown format

Ctrl - Shift - d  -> Duplicates the line of the current cursor position and creates a new line under it with the same contents

Ctrl - up/down    -> Moves the contents of the current cursor position up/down one line. If there is a line above/below with content, the current lines content will swap with the one above/below it.

Ctrl - l          -> Selects the entire line the cursor's current position is in

Ctrl - /          -> Toggles the selected text into a comment of the current grammar

Ctrl - Alt - .    -> Complete bracket

Alt - g, then d   -> Toggle list of diffs in file

Packages:  
https://atom.io/packages/merge-conflicts  
https://atom.io/packages/terminal-plus
 
