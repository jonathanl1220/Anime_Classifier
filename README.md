# Using Computer Vision and Transfer Learning to Classify Anime Characters

Below please find the link to my presentation from prezi.

**Prezi Presentation:** https://prezi.com/view/FoY8PCWQtsGkhpQoOLFA

## Table of Contents
1. [Background Information](#background-information)
2. [Data](#Data)
3. [Models](#Models)
3. [Conclusion](#conclusion)
4. [Future Steps](#future-steps)

## Background Information]

I have been watching Anime for over 20 years at this point of my life. I always found it interesting that I enjoyed watching these animated shows that required subtitles in my situation as an American born English speaker. Then I realized it isn’t just me.

Astro Boy was the first Anime that went mainstream in North America, this was in the 1960s.
Anime is a big staple even outside of Japan with 2018’s global sales revenues being around. **4.8 Billion** (with a B) USD. North America holds 42 percent of the Anime based contracts made outside of Japan. 

**What does this mean?** It means that Anime isn’t just a big deal in Japan but also in North America.

Taking my love for Anime combined with its importance to North America I decided to use computer vision to classify Anime characters.

**Why is this necessary?** 

1.	This could help future studies of what shows are similar in character design and if there is a correlation with character style and popularity.
2.	This can enhance the recommendation process by identifying character and recommending based on the image.

## Data

I used beautiful soup to scrape over 5,000 images from google images. This consist of characters from the following Animes.

**One Piece, Naruto, Bleach, Dragon Ball Z, Death Note, Black Clover, Fairy Tail, Attack On Titan, Cowboy Bebop, Full Metal Alchemist** 

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/anime_img_plot.png)

## Models

### Transfer Learning

Transfer Learning is basically utilizing an already established knowledge and using it to solve another problem.

#### VGG 19

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/VGG19.png)

To personalize this model to my data I removed the final dense layer and added a new dense layer with my class sizes.
I also used Soft Max as my activation, Categorical Cross Entropy as my Loss, and SGD as my optimizer.


#### Character Type Model

This model has 3 classes: **Male, Female, and Non-Human**

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/type_prediction_plot.png)


### Character Model

This model has 10 classes(one character from each Anime): **Beast, Yami, Ichigo, Faye, Luffy, Cell, Ryuk, Nezuko, Al, Erza**

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/char_prediction_plot.png)

#### Anime Classifier Model

This model also has 10 classes representing each Anime: **One Piece, Naruto, Bleach, Dragon Ball Z, Death Note, Black Clover, Fairy Tail, Attack On Titan, Cowboy Bebop, Full Metal Alchemist** 

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/anime_prediction_plot-1.png)

# Results

**The Type Model worked really well mainly confusing characters making exaggerated expressions.**

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/type_confu_mat.png)

**The Character Model struggled with classifying a character that was an armor knight with characters that wore armor.** 

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/char_confusion_mat_plot.png)

**The Anime Model struggled with predicting on newer Animes. The older Anime in my data was Dragon Ball Z with had the best score, whereas the newest (Demon Slayer had the worst score.** 

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/anime_confu_mat_plot.png)

## Conclusion

**I was actually happy and expected the results of the models. The models with more variance performed worst then the Type model. There is room for growth but this is a good start.**

![image](https://github.com/jonathanl1220/Anime_Classifier/blob/main/img/model_results.png)

## Future Steps

**1.Hierarchical Image Classification**

**2.Including additional Animes  and expand characters in classes.**

**3.Using different models to increase accuracy.**


