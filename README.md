# Fractals
These are the instructions for your fractal assignment. We have explored fractals from two perspectives: curves and sets. The curves we considered were from the exercises in the book. These gave us a sense of how a curve could be broken into an atomic part, and that the self-similarity was generated using the atomic part, in an algorithm. We explored trees, randomness (or lack there of) in nature, and the curves of Koch and Hilbert.

We explore both the Mandelbrot set and various Julia sets, via the articles by Tariq Rashid. These sets are constructed by considering complex numbers, and creating a sequence by iteratively applying a function, such as z^2 or z^2+c. One then considers the convergence of the sequence. If the sequence of the sequence is convergent, then we assign it a maximal number. Namely, the maximum number of iterations. The faster the divergence of the sequence, the lower the number that is assigned. We then used this data set to plot the sets via interpolation methods in matplotlib.

The goals of this assignment are to have you:
- to continue exploring the topics and concepts that we've discussed in class.
- use your own words to describe the ideas, and become more comfortable with the mathematical ideas.
- create an artifact of your learning to the larger Casady community.

You each have a different portion of the assignment. When the three of you are finished, it will provide others with an introduction to fractals in a progressive manner. Your individual assignments are listed below. While GitHub will render small Jupyter pages, these pages will be to graphically intensive, for this to be reasonable. Hence, you can create your page in a Jupyter notebook, but you will want to save the notebook as a markdown file, before pushing it to the repository.

## Kristian:
Your portion of the assignment will be to describe and explain the homework exercises, form the book. These were 10.1.1, 10.1.2, and 10.1.4. I would also like you to explore the Hilbert space-filling curve. I believe Vasili was able to get this working; so collaborate if you need assistance.

## Vasili:
Your portion of the assignment will be to explain the code and functionality in the Mandelbrot article, directly related to creating the Mandelbrot set. I would like for you to encapsulate the stand-alone code into an appropriate set of functions. Please change the for loop, in the mandel function, into an appropriate while loop.

## Armaan
Your portion of the assignment will be to explain the code in the Julia set article. I would also like for you to explain (not deeply or the why, but that it exists) the relationship between the connectedness of the Julia set, and the Mandelbrot set. You can use Wolfram Alpha to generate examples, and there is certainly some information on the web.

## Vasili & Armaan
I would like you both to explain and explore the rendering process, and things such as the different interpolation options, color maps, and blend modes. Ideally, you will coordinate and explore different aspects of these techniques. Please give a proper citation of the article you are discussing in either the first or last cell. The beginning or the end of the markdown file.

## Notes:
- GitHub does not render MathJax in the markdown files. This is unfortunate, but will have to make do. This means you will want to keep the mathematical notation to a minimum, and use notation that people are familiar with.
- If you take a hint, use information obtained from other sources than the articles or the textbook, you must cite your source. It is a violation of Casady values, and good research practices, to use data, information, or results without attribution.
- You are more than welcome to explore and include other aspects of fractals, if you have completed your portion of the assignment. I encourage you to play with code, and explore what other aspects there are to this topic.
- Keep in mind that what you create will be released to the larger community.

If you have any questions, please let me know.
