# Xiami Dataset

## Data Source                                                                                                                                                                             

This dataset contains the albums information and songs information of four most popular singers,周杰伦，林俊杰，陈奕迅，林宥嘉.

starting page:https://www.xiami.com/search?key=

## Data fields
* `歌名` - String. e.g. `可爱女人`
* `专辑名` - String. e.g. `Jay`
* `歌词` - String. e.g. `想要有直升机 想要和你飞到宇宙去 想要和你融化在一起 融化在银河里 我每天每天每天在想想想想著你`
* `演唱` - String. e.g. `周杰伦`
* `作词` - String. e.g. `徐若瑄`
* `作曲` - String. e.g. `周杰伦`
* `编曲` - String. e.g. `周杰伦`
* `分享树` - Int. e.g. `23869`
* `评论数` - Int. e.g. `2263`

## Data Volume
879 rows 9 columns

## License
CC 4.0

## obstacles and solutions

obstacle：Sometimes the host may reject the request from my application.

solution：1）open the developer tool 
          2) open the web site of [xiami]:https://www.xiami.com/ 
          3) copy the curl of the current page into the [curl]:https://curl.trillworks.com/ 
          4) replace the old headers with a new one.
