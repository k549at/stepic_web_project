#!/bin/bash
for i in `seq 1 100`;
do
   mysql -uroot -e "INSERT INTO stepic_db.qa_question (title, text, author_id, rating) VALUES ('title$i', 'text$i', '1', '$i');"
done
