create database ds4fnp;
create user ds4fnp with password 'ds4fnp';
grant all privileges on database ds4fnp to ds4fnp;
create database meltano;
grant all privileges on database meltano to ds4fnp;
create database superset;
grant all privileges on database superset to ds4fnp;