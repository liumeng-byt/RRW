# encoding=utf-8

sql_drop = "DROP TABLE IF EXISTS `user`"

sql_create = """
CREATE TABLE `user` (
  `user_id` bigint NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `dept_id` bigint DEFAULT NULL COMMENT '部门ID',
  `name` varchar(30) NOT NULL COMMENT '姓名',
  `identity` varchar(30) NOT NULL COMMENT '身份证',
  `address` varchar(120) NOT NULL COMMENT '地址',
  `job` varchar(120) NOT NULL COMMENT '职业',
  `company` varchar(120) NOT NULL COMMENT '公司',
  `user_type` varchar(2) DEFAULT '00' COMMENT '用户类型（00系统用户）',
  `email` varchar(50) DEFAULT '' COMMENT '用户邮箱',
  `phonenumber` varchar(11) DEFAULT '' COMMENT '手机号码',
  `sex` char(1) DEFAULT '0' COMMENT '用户性别（0男 1女 2未知）',
  `avatar` varchar(100) DEFAULT '' COMMENT '头像地址',
  `password` varchar(100) DEFAULT '' COMMENT '密码',
  `status` char(1) DEFAULT '0' COMMENT '帐号状态（0正常 1停用）',
  `del_flag` char(1) DEFAULT '0' COMMENT '删除标志（0代表存在 2代表删除）',
  `login_ip` varchar(128) DEFAULT '' COMMENT '最后登录IP',
  `login_date` datetime DEFAULT NULL COMMENT '最后登录时间',
  `create_by` varchar(64) DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` varchar(64) DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(500) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=200 DEFAULT CHARSET=utf8mb3 COMMENT='用户信息表';
"""

sql_insert = "INSERT INTO `user` (`dept_id`, `name`, `identity`, `address`,`job`,`company`,`user_type`, `email`, `phonenumber`, `sex`, `avatar`, " \
             "`password`, `status`, `del_flag`, `login_ip`, `login_date`, `create_by`, `create_time`, `update_by`, `update_time`, " \
             "`remark`) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, '1', '', '$2a$10$7JB720yubVSZvUI0rEqK/.VqGOZTH.ulu33dHOiBE8ByOhJIrdAu2', " \
             "'0', '0', '127.0.0.1', '2022-01-30 12:55:06', 'admin', '2022-01-30 12:35:45', '', '2022-01-30 12:55:06', '管理员');"
