# -*- coding:utf-8 -*-

#保存数据
import pandas as pd
import os

#获得当前路径的上级路径
curPath = os.path.dirname(os.getcwd())
test =[{'标题': '黑色喜剧《驴得水》武汉站', '副标题': '口碑佳作《驴得水》被许多剧迷称作"神剧"', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019-01-06', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171739, 'imgurl': '1717', '最低票价': 80.0, '最高票价': 380.0}, {'标题': 'MaiLive孟京辉戏剧作品《一个陌生女人的来信》武汉站', '副标题': '讲述陌生女人和W先生"三次做饭与三次交欢"的疯狂爱情。', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2019.05.03-05.05', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172121, 'imgurl': '1721', '最低票价': 100.0, '最高票价': 480.0}, {'标题': '开心麻花2019爆笑贺岁舞台剧《谈判专家》', '副标题': '开心麻花原创贺岁舞台剧', '地点城市': '武汉', '演出场所': '武汉剧院', '演出时间': '2019.03.07-03.10', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172146, 'imgurl': '1721', '最低票价': 100.0, '最高票价': 1320.0}, {'标题': '武汉歌舞剧院歌剧团2018年度考核', '副标题': '武汉歌舞剧院歌剧团考核是专业歌唱演员一年一度的业务评比，集专业性，观赏性于一体', '地点城市': '武汉', '演出场所': '520爱剧场', '演出时间': '2018.12.29 14:30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172230, 'imgurl': '1722', '最低票价': 30.0, '最高票价': 50.0}, {'标题': '原创话剧《这些年》', '副标题': '以小人物的视角真实质朴的展现了普通人在时代大浪中的命运变化', '地点城市': '武汉', '演出场所': '武汉人民艺术剧院-D5空间', '演出时间': '2018.12.31-2019.01.26', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172111, 'imgurl': '1721', '最低票价': 50.0, '最高票价': 50.0}, {'标题': 'MaiLive 孟京辉经典音乐剧作品《空中花园谋杀案》武汉站', '副标题': '整个城市为了空中花园而疯狂!新的谋杀即将开始……', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2019.06.28-06.30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172089, 'imgurl': '1720', '最低票价': 100.0, '最高票价': 480.0}, {'标题': 'MaiLive 孟京辉戏剧作品《我爱XXX》武汉站', '副标题': '语言本身不具备意义，却是我们生存的唯一现实，我们与它相依为命。', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2019.03.15-03.16', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172094, 'imgurl': '1720', '最低票价': 100.0, '最高票价': 480.0}, {'标题': '话剧《蒋公的面子》', '副标题': '这是一个后辈学生根据校史传说虚构的关于前辈老师和校长的故事。', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2019.04.27 19:30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172018, 'imgurl': '1720', '最低票价': 100.0, '最高票价': 870.0}, {'标题': 'MaiLive 孟京辉戏剧作品《九又二分之一爱情》武汉站', '副标题': '讲述了一个关于爱与复仇的当代寓言。', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2019.04.26-04.28', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172118, 'imgurl': '1721', '最低票价': 100.0, '最高票价': 480.0}, {'标题': '江湖爆笑喜剧《萨瓦迪大咖》', '副标题': '一条暧昧微信引发婚姻信任危机！', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2019.02.08-02.09', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172236, 'imgurl': '1722', '最低票价': 100.0, '最高票价': 380.0}, {'标题': '托马斯&朋友—迷失宝藏', '副标题': '英国儿童电视动画剧《Thomas&Friends》改编', '地点城市': '武汉', '演出场所': '武汉剧院', '演出时间': '2019.06.01', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171837, 'imgurl': '1718', '最低票价': 80.0, '最高票价': 600.0}, {'标题': '开心麻花2019爆笑贺岁舞台剧《窗前不止明月光》', '副标题': '开心麻花爆笑推荐超“毒舌”台词根本停不下来！', '地点城市': '武汉', '演出场所': '武汉剧院', '演出时间': '2019.01.18-01.19', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169863, 'imgurl': '1698', '最低票价': 100.0, '最高票价': 1320.0}, {'标题': '大型梦幻卡通舞台剧《白雪公主》', '副标题': '根据《格林童话》经典故事改编了《白雪公主》这部儿童剧', '地点城市': '武汉', '演出场所': '汤湖戏院', '演出时间': '2019.01.01', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171083, 'imgurl': '1710', '最低票价': 60.0, '最高票价': 120.0}, {'标题': '英国音乐戏剧秀《欢乐颂》', '副标题': '来自英国的JunNK剧团由四位神秘逗咖爆笑上演，', '地点城市': '武汉', '演出场所': '汤湖戏院', '演出时间': '2019.01.04', '演出状态': '售票中', '演出类型': '音乐剧', 'projectid': 171144, 'imgurl': '1711', '最低票价': 60.0, '最高票价': 120.0}, {'标题': '武汉年度C位爆笑喜剧《抹茶攻略》', '副标题': '有如手工钟表般精密的结构喜剧。', '地点城市': '武汉', '演出场所': '武汉剧院', '演出时间': '2018.12.27 19:30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 170671, 'imgurl': '1706', '最低票价': 110.0, '最高票价': 480.0}, {'标题': '儿童剧《小蝌蚪找妈妈》', '副标题': '青蛙妈妈和小蝌蚪们终于团聚。妈妈给孩子们上了有意义的人生第一课。', '地点城市': '武汉', '演出场所': '武汉人民艺术剧院-亲子剧场', '演出时间': '2018.01.05-01.27', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 170767, 'imgurl': '1707', '最低票价': 50.0, '最高票价': 50.0}, {'标题': 'MaiLive 孟京辉戏剧作品《两只狗的生活意见》武汉站', '副标题': '他们决定勇敢地面对生活，不管生活有多艰辛，一定要勇敢地走下去！', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2019.01.11-01.13', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 163615, 'imgurl': '1636', '最低票价': 100.0, '最高票价': 480.0}, {'标题': '有趣戏剧第四回 话剧《杏仁豆腐心》武汉站', '副标题': '《杏仁豆腐心》不是年轻情侣间的撕X大戏，而是想借助两颗灵魂的孤独唏嘘，找回我们原本柔软而温暖的内心。', '地点城市': '武汉', '演出场所': '403国际艺术中心·红椅剧场', '演出时间': '2019.01.05-01.06', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 170709, 'imgurl': '1707', '最低票价': 80.0, '最高票价': 280.0}, {'标题': '武汉·2019年1月大型儿童剧《白雪公主》', '副标题': '根据《格林童话》经典故事改编了《白雪公主》这部儿童剧。', '地点城市': '武汉', '演出场所': '珞珈山剧院', '演出时间': '2019.01.06', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 169845, 'imgurl': '1698', '最低票价': 39.0, '最高票价': 79.0}, {'标题': '江城爱情故事系列舞台剧《缘来是你》', '副标题': '江诚也发现了自己爷爷的日记，一段民国时期的爱情故事呈现在两人眼前……', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2018.12.21-2019.01.25', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171652, 'imgurl': '1716', '最低票价': 100.0, '最高票价': 100.0}, {'标题': '大型贺岁方言喜剧——新编《海底捞月》武汉站', '副标题': '本剧通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁。', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2018.12.16-12.30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169745, 'imgurl': '1697', '最低票价': 80.0, '最高票价': 1080.0}, {'标题': '爆笑喜剧《萨瓦迪大咖》', '副标题': '剧情是围绕从泰国回来的萨瓦迪大咖给一个家庭带来的婚姻危机展开。', '地点城市': '武汉', '演出场所': '汤湖戏院', '演出时间': '2018.12.30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169630, 'imgurl': '1696', '最低票价': 100.0, '最高票价': 280.0}, {'标题': '武汉说唱团贺岁剧2019经典再现《海底捞月》', '副标题': '通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁，传奇、暴笑、又让人感慨万千……', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2018.12.18-2019.01.02', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 168943, 'imgurl': '1689', '最低票价': 80.0, '最高票价': 480.0}, {'标题': '武汉年度C位爆笑喜剧《抹茶攻略》', '副标题': '有如手工钟表般精密的结构喜剧。', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2019.12.09-2019.01.04', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169604, 'imgurl': '1696', '最低票价': 80.0, '最高票价': 480.0}, {'标题': '2019经典再现贺岁喜剧《海底捞月》', '副标题': '本剧通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁，传奇、暴笑、又让人感慨万千', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2018.12.28-2019.01.22', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171241, 'imgurl': '1712', '最低票价': 80.0, '最高票价': 480.0}, {'标题': '武汉说唱团爆笑神剧《海底捞月》', '副标题': '本剧通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁。', '地点城市': '武汉', '演出场所': '汤湖戏院', '演出时间': '2018.12.29-2019.02.19', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169619, 'imgurl': '1696', '最低票价': 80.0, '最高票价': 180.0}, {'标题': '舞台剧《剑网3·曲云传》武汉站', '副标题': '高度还原的游戏场景和故事剧情，让你笑着流泪，哭着感动！', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019-01-13 14:30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171016, 'imgurl': '1710', '最低票价': 188.0, '最高票价': 988.0}, {'标题': '《海底小纵队4：极地大冒险》武汉站', '副标题': '英国版权引进，海洋探险故事奇幻，开发想象力，魅力无穷。', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019.01.05 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 169531, 'imgurl': '1695', '最低票价': 60.0, '最高票价': 780.0}, {'标题': '大型音乐舞台剧《犹太城》武汉站', '副标题': '讲述二战期间德国纳粹占领和控制下的维尔纽斯犹太城里发生的故事。', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019.01.20   19:30', '演出状态': '售票中', '演出类型': '歌舞剧', 'projectid': 169510, 'imgurl': '1695', '最低票价': 80.0, '最高票价': 1199.0}, {'标题': '九町舞台剧《8090》', '副标题': '', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2018.12.29-12.30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 581170117488, 'imgurl': '1516733878', '最低票价': 30.0, '最高票价': 100.0}, {'标题': '木偶剧《小马过河》', '副标题': '键时刻嗒嗒想起了爸爸的话，揭穿了狐狸的把戏，勇敢的走向河边……', '地点城市': '武汉', '演出场所': '武汉人民艺术剧院-亲子剧场', '演出时间': '2018.11.03-12.30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 166932, 'imgurl': '1669', '最低票价': 50.0, '最高票价': 50.0}, {'标题': '世界原版经典音乐剧《猫》CATS-武汉站', '副标题': '世界原版经典音乐剧《猫》2019中国“猫”年震撼回归', '地点城市': '武汉', '演出场所': '武汉剧院', '演出时间': '2019.06.21-06.26', '演出状态': '预售', '演出类型': '音乐剧', 'projectid': 172365, 'imgurl': '1723', '最低票价': 280.0, '最高票价': 1380.0}, {'标题': '冷佳华儿童戏剧工作室主题晚会“点亮童心.明天启航”', '副标题': '由一个人讲到一个剧种，由一个剧种的发展，讲述一群“儿童戏剧”工作者们的默默奉献。', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2018.12.29-12.30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171892, 'imgurl': '1718', '最低票价': 30.0, '最高票价': 160.0}, {'标题': '九町舞台剧《老婆梦工厂》', '副标题': '通过欢乐多彩的舞台呈现，讲述了"一见钟情"式的爱情体验。', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2019.01.05-01.27', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171664, 'imgurl': '1716', '最低票价': 50.0, '最高票价': 50.0}, {'标题': '小鬼当家系列亲子剧《神秘大盗》', '副标题': '寓教于乐，告诉小朋友们乐于助人、拾金不昧的教育理念', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2018.12.22-2019.01.26', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171662, 'imgurl': '1716', '最低票价': 30.0, '最高票价': 100.0}, {'标题': '九町舞台剧《游侠小红帽》', '副标题': '经典儿童剧改编，让短小平淡的故事更加丰满', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2018.12.22-2019.01.26', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171665, 'imgurl': '1716', '最低票价': 50.0, '最高票价': 50.0}, {'标题': '保利原创儿童剧《故宫里的小不点》武汉站', '副标题': '为广大小朋友及家长们带来奇幻视觉盛宴', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019.01.15 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171231, 'imgurl': '1712', '最低票价': 80.0, '最高票价': 760.0}, {'标题': '浪漫经典童话剧《灰姑娘》--武汉站', '副标题': '王子能否找到舞会上的灰姑娘？美丽的童话将在今夜绽放！', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场', '演出时间': '2019.07.06 10:30/15:00', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171179, 'imgurl': '1711', '最低票价': 50.0, '最高票价': 260.0}, {'标题': '凡创文化·大型恐龙主题实景童话剧《你看起来好像很好吃》', '副标题': '《你看起来好像很好吃》给所有的恐龙们都编排了极富童趣的舞蹈。', '地点城市': '武汉', '演出场所': '武汉剧院', '演出时间': '2019.04.14 10:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 170724, 'imgurl': '1707', '最低票价': 100.0, '最高票价': 1500.0}, {'标题': '梦幻互动亲子剧《人鱼公主》--武汉站', '副标题': '这是一次友情、亲情与爱情的启蒙童话之旅', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场', '演出时间': '2019.09.07', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171140, 'imgurl': '1711', '最低票价': 50.0, '最高票价': 260.0}, {'标题': '奇幻亲子音乐剧《绿野仙踪》--武汉站', '副标题': '华丽多变的舞蹈与原创音乐相得益彰，拉开奇幻视觉盛宴的序幕', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场', '演出时间': '2019.11.02 10:30/15:00', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171186, 'imgurl': '1711', '最低票价': 50.0, '最高票价': 260.0}, {'标题': '寻梦亲子音乐剧《Flight School 飞行学校》--武汉站', '副标题': '励志的故事，动听的音乐，让孩子在音乐剧的世界里找到乐趣，教你在友情、团结中找到梦想。', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场', '演出时间': '2019.08.10', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171157, 'imgurl': '1711', '最低票价': 50.0, '最高票价': 260.0}, {'标题': '经典成长童话《匹诺曹》--武汉站', '副标题': '经典成长童话《匹诺曹》将给观众带来感动与趣味。', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场', '演出时间': '2019.06.15  10:30/15:00', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171025, 'imgurl': '1710', '最低票价': 50.0, '最高票价': 260.0}, {'标题': '大型系列儿童剧《恐龙王国》之《恐龙王国之南极之旅》', '副标题': '一个好题材，一个好故事', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2019.01.06', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 170700, 'imgurl': '1707', '最低票价': 80.0, '最高票价': 100.0}, {'标题': '九町儿童剧《游侠小红帽》', '副标题': '《小红帽》让孩子们在接受艺术启蒙的同时，潜移默化的学会人生哲理。', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2018.12.01-12.29', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 168921, 'imgurl': '1689', '最低票价': 10.0, '最高票价': 100.0}, {'标题': '禾空间小剧场原创惊悚爆笑舞台剧——《goodbye旅行社之黑白先生》', '副标题': '如果一黑一白两个人，非要请你去他们的地盘旅游，你敢去吗？', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.12.29-2019.01.26', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 168874, 'imgurl': '1688', '最低票价': 60.0, '最高票价': 100.0}, {'标题': '《死神来了之黄泉旅行社》万圣之夜，“惊喜”来袭！', '副标题': '地狱一日游，感受百味人生！', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.12.15-12.29', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 166298, 'imgurl': '1662', '最低票价': 80.0, '最高票价': 100.0}, {'标题': '音乐剧《灰姑娘》中文版（武汉站）', '副标题': '', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019.01.03-01.04', '演出状态': '售票中', '演出类型': '音乐剧', 'projectid': 579053572399, 'imgurl': '1495568427', '最低票价': 50.0, '最高票价': 480.0}, {'标题': '沉浸式儿童体验3D游戏剧《爱丽丝梦游仙境》', '副标题': '爱丽丝从小脑袋里就装着各种奇思妙想，因为追一只揣着怀表、会说话的兔子，她掉进了树洞，开始了一段奇幻之旅。', '地点城市': '武汉', '演出场所': '荟聚购物中心外广场南大门G区停车场', '演出时间': '2018.10.01-2019.01.20', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 164159, 'imgurl': '1641', '最低票价': 88.0, '最高票价': 88.0}, {'标题': '禾空间原创亲子互动剧《神奇动物在这里》', '副标题': '本剧由《格林童话》中《金鸟》、《牧鹅女》、《金鹅》三个故事略加改编而成', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.12.23-2019.01.13', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 167809, 'imgurl': '1678', '最低票价': 59.0, '最高票价': 69.0}, {'标题': '禾空间首部原创IP人偶儿童剧《熊猫飞飞历险记2之安徒生童话城堡的迷宫》', '副标题': '熊猫飞飞一个人踏上了寻找金禾的旅程。', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2019.01.01-01.12', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 168875, 'imgurl': '1688', '最低票价': 59.0, '最高票价': 69.0}, {'标题': '禾空间儿童剧嘉年华十次卡演出票', '副标题': '多部儿童剧', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.10.01-2019.02.28', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 164857, 'imgurl': '1648', '最低票价': 199.0, '最高票价': 199.0}, {'标题': '禾空间儿童剧嘉年华《维小鲸历险记之乘风破浪》', '副标题': '虎鲸偷偷跟上了这艘神秘大船，开启了它的海洋历险。', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.12.30-2019.01.05', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 165097, 'imgurl': '1650', '最低票价': 49.0, '最高票价': 59.0}, {'标题': 'MaiLive 孟京辉经典戏剧作品《恋爱的犀牛》武汉站', '副标题': '当代中国戏剧旗帜性作品，永远的爱情圣经', '地点城市': '武汉', '演出场所': '中南剧场大剧场', '演出时间': '2019.03.29-03.31', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172122, 'imgurl': '1721', '最低票价': 100.0, '最高票价': 480.0}, {'标题': '小鬼当家系列亲子剧《神秘大盗》', '副标题': '通过经典IP剧改编，结合现代小朋友的欣赏特点，焕发全新的乐于助人、拾金不昧的教育理念', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场', '演出时间': '2018.12.08-12.29', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 168990, 'imgurl': '1689', '最低票价': 10.0, '最高票价': 100.0}, {'标题': '武汉人艺精品剧目 《泥巴人》', '副标题': '"泥巴人"搓土即成，遇水即散，或成或散全看命运之手将它去揉搓、雕琢。', '地点城市': '武汉', '演出场所': '武汉人民艺术剧院-D5空间', '演出时间': '2018.11.30-12.29', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 167597, 'imgurl': '1675', '最低票价': 50.0, '最高票价': 50.0}, {'标题': '江城首部原创IP人偶儿童剧《熊猫飞飞历险记》2.0升级版（万圣节专场）', '副标题': '泛浸没式儿童剧，打破舞台与观众席界限', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.12.19-12.29', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 166461, 'imgurl': '1664', '最低票价': 49.0, '最高票价': 59.0}, {'标题': '禾空间嘉年华儿童剧《大头爸爸和小头儿子》', '副标题': '在奇幻森林的南边，有一个奇幻小镇。发生了意想不到的事情', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.12.12-2019.01.06', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 164860, 'imgurl': '1648', '最低票价': 49.0, '最高票价': 59.0}, {'标题': '音乐剧《搭错车》武汉站', '副标题': '音乐剧坛震撼聚焦，殿堂级音乐剧《搭错车》2019年3月8日经典重现武汉！', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2019.03.08 19:30', '演出状态': '预售', '演出类型': '音乐剧', 'projectid': 172514, 'imgurl': '1725', '最低票价': 199.0, '最高票价': 999.0}]
#将列表保存在csv中
def list_to_csv(List=test, NAME='test.csv'):
    # 读取列表内容
    _data = pd.DataFrame(List)
    _data.head()

    # 保存csv,index代表是否有序列号，如果有的话，则需要加上index_label="id"，为他添加名字，不然就会出现Unnamed，header代表是否有表头
    _data.to_csv(NAME,index=False, index_label="标题",header=True, encoding='UTF-8')

    # # _data显示表头，_data.values显示表体
    # print(_data,  '\n', _data.values)


def list_to_db():
    print(1)


def csv_to_db():
    print('1')


def db_to_csv():
    print('1')


def csv_to_data():
    con = pd.DataFrame(pd.read_csv(curPath+'/res/contents.csv',header=None, encoding='UTF-8')).values
    doi = pd.DataFrame(pd.read_csv(curPath+'/res/doings.csv',header=None, encoding='UTF-8')).values
    yun = pd.DataFrame(pd.read_csv(curPath + '/res/yundong.csv', header=0, encoding='UTF-8')).values
    test = pd.DataFrame(pd.read_csv('test.csv', header=0, encoding='UTF-8'))
    #
    # print('列表数：',len(doi[468:]),'\n',doi[468])
    # print('列表数：',len(con[468:]),'\n',con[468:])
    # print('列表数：',len(yun[0:]),'\n',yun[0])


    # #测试两个表中的数据是否相同
    # c = 0
    # for i in range(402):
    #     a = doi[i+468][2]
    #     b = yun[i][1]
    #     if a==b:
    #         c +=1
    #     # break
    # print(c)

    # #看看原来的运动表是否也是这样的数字，如果是的话，再校对一遍，然后就可以添加内容了
    # _re =[]
    # for  i in range(len(con[468:])):
    #     # print(len(con[i+468]))
    #     _de =[]
    #
    #     a = eval(con[i+468][2])
    #     b= yun[i]
    #
    #     for j in range(len(a)):
    #         a[j]['title']=b[j*3+4]
    #
    #     _de.append(str(con[i + 468][0]))
    #     _de.append(str(con[i + 468][1]))
    #     _de.append(str(a).replace(' ', ''))
    #     _de.append(str(con[i + 468][3]))
    #     _de.append(str(con[i + 468][4]))
    #
    #     _re.append(_de)
    #     # print(_de)
    #     # break

    print(test[''][0])

    # return _re

    # 做完之后，去掉文本中的空格


if __name__ == '__main__':
    # csv_to_data()
    list_to_csv()
    # print(curPath)
