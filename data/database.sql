create database if not exists `agenda`;

use `agenda`;

drop table if exists `tarefa`;

create table if not exists `tarefa`( --para evitar problemas com palavras que já existem. Ex: status
    `id` int not null `auto_increment` primary key,
    `titulo` varchar(60) not null,
    `data_conclusao` datetime null
);