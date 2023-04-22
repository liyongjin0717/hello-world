create database jing_dong charset=utf8;

create table goods(
	id int unsigned primary key auto_increment not null,
	name varchar(150) not null,
	cate_name varchar(40) not null,
	brand_name varchar(40) not null,
	price decimal(10,3) not null default 0,
	is_show bit not null default 1,
	is_saleoff bit not null default 0
	);

insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default);
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default);
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);
insert into goods values(0,'x240vc 超极本','超级本','联想','4880',default,default);
insert into goods values(0,'u330p 13.3英寸超级本','超级本','联想','4299',default,default);
insert into goods values(0,'svp13226scb 触碰超极本','超级本','索尼','7999',default,default);
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default);
insert into goods values(0,'ipad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default);
insert into goods values(0,'ideacentre c340 20英寸一体电脑','台式机','联想','3499',default,default);
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default);
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果','9188',default,default);
insert into goods values(0,'at7-7414lp 台式电脑 linux','台式机','宏基','3699',default,default);
insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普','4288',default,default);
insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔','5388',default,default);
insert into goods values(0,'mac pro专业级台式电脑','服务器/工作站','苹果','28888',default,default);
insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼','6999',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);
insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm','6888',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);


select *from goods where cate_name="超级本";

查询商品的种类
select distinct cate_name from goods;
select cate_name from goods group by cate_name;

查询每种商品的信息（按商品品牌分组）
select cate_name,group_concat(name) from goods group by cate_name;
查询所有商品的平均价格保留两位小数
select round(avg(price),2) from goods;
查询每种商品的平均价格(此时是按分组后商品种类的平均价格)
select cate_name,avg(price) from goods group by cate_name;
查询每种类型的商品中最贵，最便宜、平均价和数量
select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;
查询所有价格大于平均价格的商品，并且按价格降序排序
select *from goods where price>(select avg(price) from goods) order by price desc;
查询每种类型中最贵的电脑信息
select *
from (select cate_name,max(price) as max_price from goods group by cate_name)as a 
left join goods as g 
on a.cate_name=g.cate_name and a.max_price=g.price;

创建商品分类表
create table if not exists goods_cates(
	id int unsigned primary key auto_increment,
	name varchar(40) not null
	);
不用写value
insert into goods_cates (name) select cate_name from goods group by cate_name;
goods_cates表和goods表按goods表的cate_name和goods_cates表的id相关联
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name =c.id;

insert into goods_cates(name) values('路由器'),('交换机'),('网卡');

insert into goods (name,cate_name,brand_name,price)
values ('LaserJet Pro P1606dn 黑白激光打印机',12,4,'1849');

alter table goods change cate_name cate_id int unsigned not null;

alter table goods add foreign key(cate_id) references goods_cates(id);