#!/bin/sh

#  process_cpct_definitions_bugs.sh
#  
#
#  Created by RahulCh on 22/09/21.
#
DatabaseConfig='/Users/rahulch/Downloads/arusprint01/JenkinsJobFiles/DatabaseConfig.cfg'
username=`grep -w "^DEV_DBUSER" $DatabaseConfig | cut -d"=" -f2`
password=`grep -w "^DEV_DBUSERPASSWORD" $DatabaseConfig | cut -d"=" -f2`
dbstr=`grep -w "^DEV_DB" $DatabaseConfig | cut -d"=" -f2`

if  [ ! -z "$1" ] && [ $1 == 'PROD' ]
then
    username=`grep -w "^DBUSER" $DatabaseConfig | cut -d"=" -f2`
    password=`grep -w "^DBUSERPASSWORD" $DatabaseConfig | cut -d"=" -f2`
    dbstr=`grep -w "^DB" $DatabaseConfig | cut -d"=" -f2`
    echo "Running on ARU Prod Database"
else
    echo "Running on ARU DEV Database"
fi

echo "User Name ${username}"
#echo "password ${password}"
#echo "dbstr ${dbstr}"

login="${username}/${password}@${dbstr}"
echo "login ${login}"
#sqlplus -s <<EOF
#${username}/${password}@${dbstr}

#sqlplus -s <<EOF
#${login}

sqlplus -s ${login} <<EOF > cpct_definitions.log
set linesize 32767
set feedback off
set heading off
set serveroutput on size unlimited;
spool cpct_definitions.dat
select sysdate from dual;
WHENEVER SQLERROR EXIT 1
begin
/* Call  stored procedure */
        aru_backport_cron.process_cpct_definitions();
        dbms_output.put_line('Success');
exception
 when others then
     dbms_output.put_line('Error while executing process_cpct_definitions Job ' ||sqlerrm);
  raise;
end;
/
 EXIT;
spool off;
EOF

Result=$?

echo $Result

if [[ $Result -ne 0 ]]
then
  echo "Error calling the PL/SQL procedure."
  exit $Result
else
  echo "PL/SQL Procedure executed successfully."
  exit 0
fi
