# 爱上你主播小游戏接口文档

## 全局错误码

`401`：微信未登录

`410`：不在活动时间

`500`：服务器错误



### 错误返回格式

```json
{
    "status": 401,
    "message": "请先微信登录",
    "data": null
}
```



## 获取用户信息

```http
GET /user
```

### Response Body

```json
{
    "remain": 3,
    "cards":[
        {
            "collected": true,
        	"progress": 3
        },
        {
            "collected": false,
        	"progress": 2
        }
    ]
}
```



## 抽卡

```http
PUT /card
```

### Response Body

```json
{
	"card": false,
    "index": 2,
    "finish": false,
    "winner": false,
    "info": false,
    "count":0
}
```

`card`：抽到的类型false为碎片，true为卡牌

`index`：抽到的卡牌编号，从1开始

`finish`：抽完这次是否集齐

`winner`：是否是前五个集齐的

`info`：是否填写信息

`count`：集齐人数，只有winner=true&&info=false会返回

### 错误处理

`406`：抽奖次数已用完



## 获取二维码

```http
GET /user/qrcode/{card_id}
```

### Response Body

```json
{
    "data": "base64编码的图片"
}
```

### 错误处理

`400`：card_id无效

## 助力

```http
PUT /helper
```

### Request Body

```json
{
    "user_id": 1
}
```

### Response Body

```json
{
	"message": "助力成功"
}
```



### 错误处理

`400`：user_id无效

`403`：无法给自己助力

`404`：用户不存在

`406`：今日已帮助



## 集齐后收集个人信息

```http
POST /user/info
```

### Request Body

```json
{
    "name": "姓名",
    "tel": "手机",
    "campus": "校区"
}
```

### 错误处理

`400`：手机号错误

`403`：还未集齐

`405`：已有五个人集齐

`406`：已填写过信息