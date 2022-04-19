CREATE EXTERNAL TABLE mentions9 (
GlobalEventID int,
EventTimeDate string,
MentionTimeDate string,
MentionType int,
MentionSourceName string,
MentionIdentifier int,
SentenceID int,
Actor1CharOffset int,
Actor2CharOffset int,
ActionCharOffset int,
InRawText int,
Confidence int,
MentionDocLen string,
MentionDocTone string,
MentionDocTranslationInfo string,
Extras string)
#PARTITIONED BY (year INT, month STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' 
#fields terminated by '\t'
lines terminated by '\n'
stored as textfile
LOCATION '/gdelt-spark/MENTIONS/*';
