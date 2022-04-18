INSERT INTO COURSE VALUES(1, '資料庫系統', '資訊類', '資管系必修課', 20.00, '中文');
INSERT INTO COURSE VALUES(2, '日文入門', '語言類', '日文是現今相當熱門的語言', 15.00, '日文');
INSERT INTO COURSE VALUES(3, '英文口說', '語言類', '英文是現今相當熱門的語言', 25.00, '英文');
INSERT INTO COURSE VALUES(4, '微積分', '工程類', '微積分是工學院必備的課程', 20.00, '英文');
INSERT INTO COURSE VALUES(5, '巨量分析', '資訊類', '資管系必修課', 25.00, '中文');
INSERT INTO COURSE VALUES(6, '普通生物學', '生科類', '生科系必修課', 15.00, '中文');
INSERT INTO COURSE VALUES(7, '國文(一)', '語言類', '中文系必修課', 15.00, '中文');

INSERT INTO CHAPTER VALUES(1, '正規化', 1);
INSERT INTO CHAPTER VALUES(2, 'ERD', 1);
INSERT INTO CHAPTER VALUES(3, '機器學習介紹', 5);
INSERT INTO CHAPTER VALUES(4, '50音介紹', 2);
INSERT INTO CHAPTER VALUES(5, '口說介紹', 3);
INSERT INTO CHAPTER VALUES(6, '口說ch1', 3);
INSERT INTO CHAPTER VALUES(7, '微積分介紹', 4);
INSERT INTO CHAPTER VALUES(8, '何謂生物學', 6);
INSERT INTO CHAPTER VALUES(9, '紅樓夢', 7);


INSERT INTO QUIZ VALUES(1, '選擇題', '~/tmp/ch5/quiz1.txt', 5);
INSERT INTO QUIZ VALUES(2, '問答題', '~/tmp/ch2/quiz1.pdf', 2);
INSERT INTO QUIZ VALUES(3, '選擇題', '~/tmp/ch1/quiz1.pdf', 1);
INSERT INTO QUIZ VALUES(4, '選擇題', '~/tmp/ch3/quiz1.pdf', 3);
INSERT INTO QUIZ VALUES(5, '選擇題', '~/tmp/ch4/quiz1.pdf', 4);
INSERT INTO QUIZ VALUES(6, '問答題', '~/tmp/ch5/quiz2.pdf', 5);
INSERT INTO QUIZ VALUES(7, '選擇題', '~/tmp/ch6/quiz1.pdf', 6);
INSERT INTO QUIZ VALUES(8, '選擇題', '~/tmp/ch7/quiz1.pdf', 7);
INSERT INTO QUIZ VALUES(9, '選擇題', '~/tmp/ch8/quiz1.pdf', 8);
INSERT INTO QUIZ VALUES(10, '問答題', '~/tmp/ch8/quiz2.pdf', 8);


INSERT INTO CONTENT VALUES(1, 'pdf', '1', '5.5', '~/content/ch1/hw1.pdf', 1);
INSERT INTO CONTENT VALUES(2, 'pdf', '1', '4.5', '~/content/ch2/hw1.pdf', 2);
INSERT INTO CONTENT VALUES(3, 'ppt', '0', '3', '~/content/ch1/hw2.ppt', 1);
INSERT INTO CONTENT VALUES(4, 'word', '1', '7.5', '~/content/ch5/hw1.docs', 5);
INSERT INTO CONTENT VALUES(5, 'word', '1', '2.5', '~/content/ch1/hw3.docs', 1);
INSERT INTO CONTENT VALUES(6, 'pdf', '0', '4.5', '~/content/ch2/hw2.pdf', 2);
INSERT INTO CONTENT VALUES(7, 'pdf', '0', '3.1', '~/content/ch3/hw1.pdf', 3);
INSERT INTO CONTENT VALUES(8, 'pdf', '1', '3.2', '~/content/ch4/hw1.pdf', 4);
INSERT INTO CONTENT VALUES(9, 'pdf', '0', '3.3', '~/content/ch5/hw2.pdf', 5);
INSERT INTO CONTENT VALUES(10,'pdf', '1', '3.4', '~/content/ch6/hw1.pdf', 6);
INSERT INTO CONTENT VALUES(11,'pdf', '0', '3.5', '~/content/ch7/hw1.pdf', 7);
INSERT INTO CONTENT VALUES(12,'pdf', '1', '3.6', '~/content/ch8/hw1.pdf', 8);
INSERT INTO CONTENT VALUES(13,'pdf', '1', '3.7', '~/content/ch9/hw1.pdf', 9);
INSERT INTO CONTENT VALUES(14,'pdf', '1', '3.8', '~/content/ch9/hw2.pdf', 9);
INSERT INTO CONTENT VALUES(15,'word', '1', '3.9', '~/content/ch3/hw2.pdf', 3);
INSERT INTO CONTENT VALUES(16,'word', '0', '4.0', '~/content/ch4/hw2.pdf', 4);


INSERT INTO INSTRUCTOR VALUES(1, 'tiger', 's1233456@gmail.com', 'test123', to_date('2022-03-01', 'YYYY-MM-DD'), '你好我叫老虎');
INSERT INTO INSTRUCTOR VALUES(2, 'dragon', 's123532@gmail.com', 'Test123', to_date('2021-02-05', 'YYYY-MM-DD'), '你好我是龍');
INSERT INTO INSTRUCTOR VALUES(3, 'ren', 's2342532@gmail.com', '234twe', to_date('2020-01-25', 'YYYY-MM-DD'), '你好我是人');
INSERT INTO INSTRUCTOR VALUES(4, 'lai', 's2342@gmail.com', 'gr23423', to_date('2019-08-12', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(5, 'ky', 's2341@gmail.com', 'gr23wef423', to_date('2016-03-12', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(6, 'ct', 's2343@gmail.com', 'gr2323423', to_date('2019-01-13', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(7, 'boye', 's2344@gmail.com', 'gr2vdv3423', to_date('2011-02-16', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(8, 'wsu', 's2345@gmail.com', 'gr234agda23', to_date('2018-01-24', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(9, 'wejf', 's2346@gmail.com', 'gr23sdafa423', to_date('2012-03-16', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(10, 'wcsc', 's23427@gmail.com', 'gr2gasd3423', to_date('2017-12-12', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(11, 'fwdfs', 's23428@gmail.com', 'gr2adsf3423', to_date('2015-02-14', 'YYYY-MM-DD'), '大家好');
INSERT INTO INSTRUCTOR VALUES(12, 'dlgsa', 's23429@gmail.com', 'gr23wrqr423', to_date('2017-03-16', 'YYYY-MM-DD'), '大家好');


INSERT INTO STUDENT VALUES(1, 'lailai', 'd12334@gmail.com', '2523gfw', to_date('2015-01-26', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(2, 'leelee', 'd234532@gmail.com', '234dsfs', to_date('2013-12-01', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(3, 'renren', 'd23532@gmail.com', 'efw23r', to_date('2013-01-08', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(4, 'goodgood', 'g23523@gmail.com', 'sdg23', to_date('2021-02-18', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(5, 'gsdfg', 'g23523@gmail.com', 'werhwsdg23', to_date('2015-03-18', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(6, 'sdfg', 'g23rderw523@gmail.com', 'grhjsdg23', to_date('2022-01-01', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(7, 'qererqg', 'g23ewgrrgb523@gmail.com', 'qetrgsdg23', to_date('2015-01-13', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(8, 'jrjety', 'g235ngfne23@gmail.com', 'seqggdg23', to_date('2011-02-12', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(9, 'kyukt', 'g235wrhwrhtt23@gmail.com', 'sdh54j5jg23', to_date('2016-02-15', 'YYYY-MM-DD'));
INSERT INTO STUDENT VALUES(10, 'ewrgf', 'g23wtrhtr523@gmail.com', 'sdrg23', to_date('2019-10-23', 'YYYY-MM-DD'));

INSERT INTO PAYMENT VALUES(1, to_date('2015-01-26', 'YYYY-MM-DD'), 20.0, '2341');
INSERT INTO PAYMENT VALUES(2, to_date('2014-01-01', 'YYYY-MM-DD'), 20.0, '1245');
INSERT INTO PAYMENT VALUES(3, to_date('2021-03-20', 'YYYY-MM-DD'), 20.0, '5235');
INSERT INTO PAYMENT VALUES(4, to_date('2016-01-26', 'YYYY-MM-DD'), 20.0, '5134');
INSERT INTO PAYMENT VALUES(5, to_date('2016-01-29', 'YYYY-MM-DD'), 15.0, '7346');
INSERT INTO PAYMENT VALUES(6, to_date('2015-01-27', 'YYYY-MM-DD'), 25.0, '8436');
INSERT INTO PAYMENT VALUES(7, to_date('2017-01-26', 'YYYY-MM-DD'), 20.0, '9664');
INSERT INTO PAYMENT VALUES(8, to_date('2014-01-01', 'YYYY-MM-DD'), 15.0, '4572');
INSERT INTO PAYMENT VALUES(9, to_date('2017-01-26', 'YYYY-MM-DD'), 15.0, '7413');


INSERT INTO ENROLL VALUES(1, 1, 1, to_date('2015-01-26', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(1, 3, 2, to_date('2014-01-01', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(1, 4, 3, to_date('2021-03-20', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(1, 6, 4, to_date('2016-01-26', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(2, 8, 5, to_date('2016-01-29', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(3, 7, 6, to_date('2015-01-27', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(4, 5, 7, to_date('2017-01-26', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(7, 2, 8, to_date('2014-01-01', 'YYYY-MM-DD'));
INSERT INTO ENROLL VALUES(7, 9, 9, to_date('2017-01-26', 'YYYY-MM-DD'));



INSERT INTO COURSEINSTRUCTOR VALUES(4, 3);
INSERT INTO COURSEINSTRUCTOR VALUES(3, 2);
INSERT INTO COURSEINSTRUCTOR VALUES(3, 1);
INSERT INTO COURSEINSTRUCTOR VALUES(1, 12);
INSERT INTO COURSEINSTRUCTOR VALUES(2, 3);
INSERT INTO COURSEINSTRUCTOR VALUES(1, 11);
INSERT INTO COURSEINSTRUCTOR VALUES(5, 4);
INSERT INTO COURSEINSTRUCTOR VALUES(6, 7);
INSERT INTO COURSEINSTRUCTOR VALUES(7, 8);


INSERT INTO STUDENTQUIZ VALUES(3, 3, to_date('2015-02-26 16:30', 'YYYY-MM-DD HH24:MI'), to_date('2015-02-26 18:31', 'YYYY-MM-DD HH24:MI'), 100);
INSERT INTO STUDENTQUIZ VALUES(4, 3, NULL, NULL, NULL);
INSERT INTO STUDENTQUIZ VALUES(5, 8, to_date('2017-02-15 03:30', 'YYYY-MM-DD HH24:MI'), to_date('2017-02-15 05:21', 'YYYY-MM-DD HH24:MI'), 60);
INSERT INTO STUDENTQUIZ VALUES(7, 7, to_date('2015-02-13 07:20', 'YYYY-MM-DD HH24:MI'), to_date('2015-02-13 09:31', 'YYYY-MM-DD HH24:MI'), 70.5);
INSERT INTO STUDENTQUIZ VALUES(1, 3, NULL, NULL, NULL);
INSERT INTO STUDENTQUIZ VALUES(8, 5, to_date('2016-02-13 09:15', 'YYYY-MM-DD HH24:MI'), to_date('2016-02-13 09:31', 'YYYY-MM-DD HH24:MI'), 80.21);
INSERT INTO STUDENTQUIZ VALUES(6, 3, to_date('2022-03-01 17:50', 'YYYY-MM-DD HH24:MI'), to_date('2022-03-01 19:57', 'YYYY-MM-DD HH24:MI'), 50);


INSERT INTO STUDENTCONTENT VALUES(3, 2, to_date('2015-01-26', 'YYYY-MM-DD'), to_date('2015-11-20', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(4, 2, to_date('2022-01-12', 'YYYY-MM-DD'), null, 'not yet');
INSERT INTO STUDENTCONTENT VALUES(4, 1, to_date('2021-03-20', 'YYYY-MM-DD'), to_date('2021-03-22', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(1, 3, to_date('2015-01-26', 'YYYY-MM-DD'), null, 'not yet');
INSERT INTO STUDENTCONTENT VALUES(2, 14, to_date('2014-01-01', 'YYYY-MM-DD'), to_date('2021-01-22', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(5, 11, to_date('2017-01-26', 'YYYY-MM-DD'), to_date('2018-03-22', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(9, 13, to_date('2017-01-26', 'YYYY-MM-DD'), null, 'not yet');
INSERT INTO STUDENTCONTENT VALUES(7, 10, to_date('2015-01-27', 'YYYY-MM-DD'), to_date('2015-03-14', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(3, 6, to_date('2016-01-26', 'YYYY-MM-DD'), to_date('2017-06-30', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(7, 4, to_date('2017-01-29', 'YYYY-MM-DD'), to_date('2017-06-30', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(6, 5, to_date('2022-02-15', 'YYYY-MM-DD'), to_date('2022-03-12', 'YYYY-MM-DD'), 'finish');
INSERT INTO STUDENTCONTENT VALUES(8, 16, to_date('2016-01-29', 'YYYY-MM-DD'), to_date('2017-03-30', 'YYYY-MM-DD'), 'finish');
