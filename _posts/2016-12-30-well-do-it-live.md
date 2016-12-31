---
layout: post
title: We'll Do It Live!
date: 2016-12-30 21:26:30
description: Code at rest is a dreary thing. Worse, it's often ignored. Distributing your lifeless code is nice and all, but running it for others can be even better.
---
Code at rest is a dreary thing. Worse than that, it's ignored.

Software is wondrous because it can be distributed for pennies, and with open-source software, licensed for free. However, source code or even binaries don't *do* anything unless they're *run*. Knowing how to can be tricky, you need to have the proper environment. The quality of documentation varies, and what's obvious to the people with the skills to develop a tool, is not to those that may want to install it.

Case in point, me trying to do up a blog on GitHub Pages. `jekyll build`? No, need Jekyll installed. Docs say use Bundler. Bundler doesn't support Ruby 2.0. How do I upgrade Ruby on OS X, and should I? Maybe use RVM, that's maybe like pyvenv? OK, kinda works, using the "minimal" theme, still don't know how/why it's hitting GitHub and throwing rate limit errors at me.

This is from someone that raves about Python, is reasonably skilled with it, and perversely enjoys stepping over those sorts of hurdles. Thankfully, none of that is needed. GitHub provides the service to build your pages for you, no Ruby required. Hell, *you don't even need Git,* just a browser and some time.

Providing software as a service (and keeping that service up) makes sense to me as an engineer, loath as I am to bandy about that buzzword. Users don't need to set up a finnicky environment that is liable to break because some library got upgraded past where its version was pinned, and providers are able to get their tools used, seeing how they run and where they break.

Web apps are king. Putting your awesome, bespoke tools up on the web for anyone with a browser to use is one of the best forms of advertising, and something I'd strongly suggest my academic colleagues do whenever possible. Despite the protestations of a former advisor, successful academics are heavily engaged in marketing. Reading the trends and trying to fulfill the needs of *Nature*, et al. to get published. Put a URL in your paper and say *"try me now!"*: get that code running and *moving*.