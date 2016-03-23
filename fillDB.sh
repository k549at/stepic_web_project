#!/bin/bash
for i in `seq 1 100`;
do
   mysql -uroot -e "INSERT INTO stepic_db.qa_question (title, text, author_id, rating, id) VALUES ('title$i', 'text$i', '1', '0', '$i'); insert into stepic_db.qa_answer(text, question_id, author_id) values ('answer$i', '$i','1');"

done
