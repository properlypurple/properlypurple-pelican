Title: New site
Date: 2023-04-20 11:02
Author: properlypurple
Category: Blog, Website
Tags: pelican, python, programming 
Slug: new-site
Status: published
Series: New site design

Long time no see. 😬

If you have been on this site before, you'd notice that it looks different. Well, it not only looks different, it's also built in a very different way.

A few months ago, I started exploring something called static site generators, mainly for building the website for a side project. During this, I tested a number of options, including Gatsby, Nuxt, Hugo, Jekyll, and more. In the end, I went with this amazing option called Pelican. It's an SSG built with Python, which is a language very close to my heart.

I intend to go over the options I had, how they compare, and the process for building this site with pelican. This is going to be a series of blog posts, with a lot of technical stuff. It's not meant to be a comprehensive resource for choosing a site-building tool, or building with Pelican. This is mainly meant to be a place for me to document my process.

### Why

I've been using WordPress for a long time, and I work with WordPress as my daily job. It's an obvious choice for building a site then, right? Well, yes and no. WordPress is an amazing tool, but I wanted to be able to go back to basics for this site. I've used WordPress on this site forever, and I felt like experimenting with something else.

### Options, options, options

If you go out and search for a site building tool in 2023, you will find hundreds of options. Even with static site generators, there are so many choices, that one might get overwhelmed and give up altogether. My few requirements were (in no particualr order) :

- Easy export of content from WordPress
- A programming language that I can understand
- Lightweight output
- Ease of use
- Something that's actively developed
- Ease of deployment
- Version control

My current choice — Pelican — ticks all of these, and a few more.

### What did I consider

I went through a number of options, and I'll go through them down below.

#### Hugo

This was my top choice. It's easy to use, has plenty of themes and community support available, works well, and has generally good reactions.

Having said that, I'm not really a fan of Go, and have no desire to learn it, if I need to dive in and make custom stuff.

#### Gastsby

Another great option, but it outputs a single page js application, and I'm trying to avoid that much javascript. Some other options such as Nuxt etc have the same issue for me,

#### Zola

Zola is an interesting project, and ticks most of the boxes. Rust is also a language that I'm willing to learn for other things. After some experimentation, it turns out that [Zola doesn't support dates in blog post urls](https://github.com/getzola/zola/issues/635)

### Pelican

When I looked throught it, it felt a little difficult to approach. However, the documentation is extensive, and there are a number of plugins available to add functionality. It's super-simple to get set up, and I was up and running with a custom barebones theme in no time.

I have spent quite some time on this, and the source code for this site can be found on my Github profile. This is supposed to be a series, and I'm going to talk more about the actual process in the next few blog posts.

