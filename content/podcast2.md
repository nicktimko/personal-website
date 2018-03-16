Title: Transforming Audio into Feature Vectors
Date: 2018-03-15 23:47:00
Category: Blog
Slug: podcast-filter-2
Summary: In this installment, I try to convert audio into something I can put into a machine learning classifier.

Continuing on with the ChiPy mentorship Python project, I've been trying to create a filter that will remove ads from podcasts. My first attack plan was to do speaker identification on the NPR ad reader, as any time his voice is present, it's a sponsorship spot. Step one was to generate two piles of classified data: 1) the ads, and 2) the podcasts sans ads. An hour or so with Audacity made short work of that, which, as far as data science goes, is pretty quick to collect a healthy amount of data.

The next part of the data science pipeline is the fun part: cleaning. I'm maybe loosely using the term here as I need to at a minimum transform the time-domain signal into frequency space. Humans rarely notice phase in their audio signals, and mixers, sampling and encoding schemes can upset it. How do we apply the Fourier transform though? Following along with a couple papers including Reynolds and Rose, we first break the original time signal into a series of "frames", each lasting about 20-40 milliseconds. The line of thinking is that in that period of time, there will be minimal change in the frequency content of the signal. Mouths don't move that fast.

Backing up slightly, we also apply a pre-emphasis filter to the signal which has the effect of boosting high frequencies. Lower frequencies tend to have more power, trailing off with the harmonics. This could be done either before or after the Fourier transform, but a simple two-term infinite-impulse response (feedback) filter also serves.

Stacking up the result of some Fourier transforms for each frame results in an abstract-looking figure below. From it we can glean some insight: there is a strong frequency component around 600-800 Hz with a couple harmonic peaks above it. Frequencies above a couple thousand hertz likely come from harsh consonant sounds like S's or abrupt plosives like P's.

![fig1]({filename}/images/blog2-fig1.png)

In order to transform the entire frame's worth of frequencies into a smaller feature vector, the power of the signal across a group of frequencies are added. The frequency groups are determined by windows that are perceptually uniform, and are more formally known as a Mel-frequency filterbank.

![fig2]({filename}/images/blog2-fig2.png)

Combining those 30 filters with the original audio signal results in a compressed spectrogram with hopefully more useful information at each point in time.

![fig3]({filename}/images/blog2-fig3.png)

For the next steps, I'll try to throw my 30-dimensional vectors at some machine learning models and see if the transforms and amount of data are sufficient to identify a person. My hope is that because the audio is remarkably clean and I can use fairly conservative heuristics once I tag unknown data, I'm at least close.
