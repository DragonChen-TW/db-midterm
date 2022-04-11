DROP TABLE COURSE CASCADE CONSTRAINTS;
DROP TABLE CHAPTER CASCADE CONSTRAINTS;
DROP TABLE QUIZ CASCADE CONSTRAINTS;
DROP TABLE CONTENT CASCADE CONSTRAINTS;
DROP TABLE INSTRUCTOR CASCADE CONSTRAINTS;
DROP TABLE STUDENT CASCADE CONSTRAINTS;
DROP TABLE PAYMENT CASCADE CONSTRAINTS;
DROP TABLE ENROLL CASCADE CONSTRAINTS;
DROP TABLE COURSEINSTRUCTOR CASCADE CONSTRAINTS;
DROP TABLE STUDENTQUIZ CASCADE CONSTRAINTS;
DROP TABLE STUDENTCONTENT CASCADE CONSTRAINTS;

CREATE TABLE COURSE (
    course_id    CHAR(10)      NOT NULL,
    title        VARCHAR(50)   NOT NULL,
    category     VARCHAR(30),
    brief        VARCHAR(100),
    course_fee   DECIMAL(7, 2),
    language     VARCHAR(30),
    PRIMARY KEY (course_id)
);

CREATE TABLE CHAPTER (
    chapter_id       CHAR(10)       NOT NULL,
    chapter_title    VARCHAR(50),
    course_id        CHAR(10)      NOT NULL,
    PRIMARY KEY(chapter_id),
    FOREIGN KEY(course_id)
    REFERENCES COURSE(course_id)
);

CREATE TABLE QUIZ (
    q_id       CHAR(10)      NOT NULL,
    type       VARCHAR(30),
    path       VARCHAR(100),
    chapter_id CHAR(8)      NOT NULL,
    PRIMARY KEY(q_id),
    FOREIGN KEY(chapter_id)
    REFERENCES CHAPTER(chapter_id)
);

CREATE TABLE CONTENT (
    content_id     CHAR(10)      NOT NULL,
    type           VARCHAR(30),
    is_mandatory   NUMBER(1),
    required_time  DECIMAL(6, 2),
    file_path      VARCHAR(100),
    chapter_id     CHAR(8),
    PRIMARY KEY (content_id),
    FOREIGN KEY (chapter_id)
    REFERENCES CHAPTER(chapter_id)
);

CREATE TABLE INSTRUCTOR (
    i_id                 CHAR(10)        NOT NULL,
    name                 VARCHAR(20),
    email                VARCHAR(40),
    password             VARCHAR(20),
    register_date        DATE,
    introduction_brief   VARCHAR(100),
    PRIMARY KEY(i_id) 
);

CREATE TABLE STUDENT (
    s_id                CHAR(10)          NOT NULL,
    name                 VARCHAR(20),
    email                VARCHAR(40),
    password             VARCHAR(20),
    register_date        DATE,
    PRIMARY KEY(s_id)
);

CREATE TABLE PAYMENT (
    p_id    CHAR(10)    NOT NULL,
    p_date    DATE,
    amount  INT,
    card_id CHAR(4),
    PRIMARY KEY(p_id)
);

CREATE TABLE ENROLL (
    course_id    CHAR(10)       NOT NULL,
    s_id         CHAR(10)       NOT NULL,
    p_id         CHAR(10),
    e_date         DATE,
    PRIMARY KEY(course_id, s_id),
    FOREIGN KEY(s_id) REFERENCES STUDENT(s_id),
    FOREIGN KEY(p_id) REFERENCES PAYMENT(p_id)
);

CREATE TABLE COURSEINSTRUCTOR (
    course_id   CHAR(10)       NOT NULL,
    i_id        CHAR(10)       NOT NULL,
    PRIMARY KEY(course_id, i_id),
    FOREIGN KEY(course_id) REFERENCES COURSE(course_id),
    FOREIGN KEY(i_id) REFERENCES INSTRUCTOR(i_id)
);

CREATE TABLE STUDENTQUIZ (
    s_id      CHAR(10)        NOT NULL,
    q_id      CHAR(10)        NOT NULL,
    PRIMARY KEY(s_id, q_id),
    FOREIGN KEY (s_id) REFERENCES STUDENT(s_id),
    FOREIGN KEY (q_id) REFERENCES QUIZ(q_id)    
);

CREATE TABLE STUDENTCONTENT (
    s_id           CHAR(10)       NOT NULL,
    content_id     CHAR(10)       NOT NULL,
    PRIMARY KEY(s_id, content_id),
    FOREIGN KEY(s_id) REFERENCES STUDENT(s_id),
    FOREIGN KEY(content_id) REFERENCES CONTENT(content_id)
);