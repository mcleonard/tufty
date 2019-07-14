# Tufty, friendly data visualization in Python

First up, these are **my opinions** on the current data visualization ecosystem in Python.

Matplotlib is the tried and true workhorse of Python data visualization. It definitely has some issues, mostly due to being based on MatLab's plotting interface. It has a weird combination of two different APIs which can be difficult for beginners to pick up. Of all the Python plotting libraries, it has the most flexibility and power, but it can be difficult to make attractive looking figures. As [Jake VanderPlas joked](https://twitter.com/jakevdp/status/964515238702755841?s=20)
> matplotlib really is an amazingly powerful tool... you give me any visualization, and I bet I could exactly reproduce it in matplotlib with only a few weeks of tinkering.

Seaborn is built on top of Matplotlib and makes beautiful figures. However, I feel that the API is unintuitive. I find myself having to look up the documentation anytime I want to plot something. I think it helped the ecosytem in showing that your figures don't have to be ugly by default. It's also really cool the way it works with Pandas DataFrames.

Altair is new and really impressive, but I'm not a fan of the declarative API. The easy interactivity is a huge feature. Altair is really cool, go try it out.

Plotly and Bokeh both feel heavy compared to Matplotlib. Most of the time I don't need a fancy, slow interface attached to my plots. I want a scatter plot and I want it as fast and straightforward as possible.

## Enter Tufty

I am trying to build a new data viz library that improves on what already exists in multiple ways. I want to take all the good things and mush them into one excellent package. My goals with Tufty:

- Attractive figures by default, with minimal effort
- Intuitive (imperative) API that does what you expect, in as few lines of code as possible
- Built on top of Matplotlib so users can dive in to the details if needed 
- API can use fields from Pandas DataFrames similar to Seaborn

Let's see how successful I am with this.

## Dependencies

Python 3.6+, matplotlib, and pandas