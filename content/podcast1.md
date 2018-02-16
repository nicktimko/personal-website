Title: First Steps towards the Proxy Podcast Ad Blocker
Date: 2018-02-15 23:03:00
Category: Blog
Slug: podcast-filter-1
Summary: Podcasts are breaking into the mainstream, bringing with them hordes of ads. Can we do something about it?

Podcasts are starting to break into the mainstream, and increasingly seen by advertisers as a way to get a message to a self-selected, semi-captive audience. I currently have 36 podcasts I'm subscribed to, and the uptick in ads has been noticeable. If only there was a way to remove them, maybe with some data analysis...

As part of the ChiPy mentorship program for Spring 2018, I'm endeavouring to work on a project that I've thought about for quite some time but resisted some of my crude initial attempts: a podcast ad filter. The goal that I've set out to do is create a server that I can point my podcast app at, and have it re-host (privately) a version of the audio file with some or all of the ads removed. The server components and getting the file should be straightforward, so the bulk of development time will be focused on identifying ads.

## Strategies

There are a couple strategies that I forsee that could be used to identify ads. In estimated order of ease:

1. Speaker Identification

    Podcast networks like [NPR](http://nationalpublicmedia.com/npr/platforms/npr-podcasts/) have a dedicated ad-reader who is never a reporter or host of the story. Using speaker identification, we can delineate segments with their voice and drop them.

2. Audio Fingerprinting for Music/Stings

    Networks like Gimlet Media have characteristic "ad music" that plays under advertisements read by the hosts, for example [Reply All](https://www.gimletmedia.com/reply-all). Speaker identification can't be used as it would give a false positive on content, but we could fingerprint the songs that are used and exclude segments with them. Similarly, some podcasts like [APM's Marketplace](https://www.marketplace.org/) have a distinctive sting that plays at the beginning. Find that and drop the pre-roll.

3. Natural Language Processing

    Podcasts where the host reads ads and no underlying music are more tricky. Speech-to-text in combination with NLP could be used to find "ad-like" content, but this is probably a bit of a bear. [Midroll](http://www.midroll.com/) is an advertiser in this space.

## Initial Focus: Speaker Identification

Here I'll start. One of the reasons is because I forsee getting data will be pretty quick: download a bunch of NPR podcasts, and use Audacity to chop them up into ad segments and clean segments. The number of segments will be fairly low, but the total length should be a healthy amount in the hundreds of seconds that I can cut up a thousand ways.

Initial research in this space popped up [a 1995 paper by Reynolds and Rose](http://www.cs.toronto.edu/~frank/csc401/readings/ReynoldsRose.pdf), *Robust Text-Independent Speaker Identification Using Gaussian Mixture Models*. As a first approximation, the frequency content of someone's speech reflects the average shape of their vocal tract. Nitty-gritty details like how big to make the FFT window, should they overlap, how to transform the output I need to scrape out of the methods section.

Beyond Reynolds, I still have more reading to do, and as usual when jumping into a field of research, papers form a web of science and I need to crawl through it a bit more. Fun awaits!
