# NLP_Chinese

> Application for processing Chinese text : Sentiment , Keywords , Abstract

## Usage

```shell
python nlpChinese.py news
```

- **nlpChinese.py**: entry
- **news**: the fold for news texts

## Requirement

Python 2.7 or 3.5 or latest

## Output

```
{
  "文件名":{
    "code": 状态码，目前还未添加直接写了1,
   	"sentiment": -1-1的浮点数，接近于1为积极，-1为消极,
    "title": 题目,
    "abstract": 摘要,
    "time": 时间
    "keywords":[
      {
        "frequency": 词频,
    	"word": 关键词
      },
    ...
    ],
  "message":success or error
  },
...
}
```



for example:

```json
{
    "news_test_0.txt": {  
        "code": 1,
        "sentiment": -0.5913626456902517,
        "tilte": "河南一精神病院患者用筷子袭击女患者，致三死一重伤",
        "abstract": "事件造成3名女性精神病患者死亡 杨某某被转移到医院过程中 杨某某家属与大众医院联系 并与医院工作人员一同将杨某某转移安置到该院“四防”病区 63岁的女患者云某某已死亡 ",
        "time": "2017-04-01 19:57",
        "keywords": [
            {
                "frequency": 19,
                "word": "患者"
            },
            {
                "frequency": 10,
                "word": "某某"
            },
            {
                "frequency": 12,
                "word": "精神病"
            },
            {
                "frequency": 12,
                "word": "医院"
            },
            {
                "frequency": 13,
                "word": "洛宁县"
            }
        ],
        "message": "sucess"
    },
    "news_test_1.txt": {
        "code": 1,
        "sentiment": 0.9947093760814028,
        "tilte": "韩国军方：朝鲜今晨发射1枚弹道导弹 飞行距离约60公里",
        "abstract": "朝鲜当天上午在咸镜南道新浦一带朝向半岛东部海域发射不明飞行物 因此当天发射的飞行物为潜射导弹的可能性较小 该飞行物为1枚弹道导弹 这是朝鲜于3月22日发射弹道导弹遭失败后时隔14天再次发射飞行物 朝方当天上午6时40分许发射的该飞行物 ",
        "time": "2017-04-05 07:02:00",
        "keywords": [
            {
                "frequency": 8,
                "word": "发射"
            },
            {
                "frequency": 6,
                "word": "道"
            },
            {
                "frequency": 8,
                "word": "飞行"
            },
            {
                "frequency": 5,
                "word": "朝鲜"
            },
            {
                "frequency": 5,
                "word": "导弹"
            }
        ],
        "message": "sucess"
    }
}
```



## Reference

[SnowNLP](https://github.com/isnowfy/snownlp)

## ToDo

- [ ] Process the errors
- [ ] News training text

## Contact

i@idejie.com