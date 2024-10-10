create database LMSys;
use LMSys;

show tables;
select * from auth_user;
select * from centralscentralserverapp_licenseerverapp_license;

SELECT `centralserverapp_license`.`id`,
    `centralserverapp_license`.`licenseKey`,
    `centralserverapp_license`.`isActive`,
    `centralserverapp_license`.`createdAt`,
    `centralserverapp_license`.`updatedAt`,
    `centralserverapp_license`.`expirationDate`,
    `centralserverapp_license`.`user_id`
FROM `lmsys`.`centralserverapp_license`;
