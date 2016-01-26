
library(ggplot2)
library(reshape2)

fig5a <- read.csv("histogramBroncoComments.csv")
p <- ggplot(fig5a, aes(x =Num_Replies_Bronco, y =Occurances)) + geom_bar(stat = "identity")  + theme_bw(base_size=20, base_family="Helvetica")

(p)






library(ggplot2)
library(scales)

x <- seq(0, 4 * pi, 0.1)
n <- length(x)
y1 <- 0.5 * runif(n) + sin(x)
y2 <- 0.5 * runif(n) + cos(x) - sin(x)+cos(x)
y3 <- 0.5 * runif(n) + cos(x) - sin(x)

plot(x, y1, col = "blue", pch = 20)
points(x, y2, col = "red", pch = 20)
points(x, y3, col = "green", pch = 20)


post_dataBronco=read.csv("participationRateBronco.csv")
year=post_dataBronco$year
yBronco=post_dataBronco$rate



post_dataBronco=read.csv("participationRateBronco.csv")
year=post_dataBronco$year
yBronco=post_dataBronco$rate

post_data1=read.csv("participationRate_1.csv")
year=post_data1$year
yUser1=post_data1$rate

post_data2=read.csv("participationRate_2.csv")
year=post_data2$year
Comments_Per_Bronco_Post=post_data2$rate

post_data3=read.csv("participationRate_3.csv")
year=post_data3$year
yUser3=post_data3$rate

post_data4=read.csv("participationRate_4.csv")
year=post_data4$year
yUser4=post_data4$rate

post_data5=read.csv("participationRate_5.csv")
year=post_data5$year
yUser5=post_data5$rate

post_data5=read.csv("postsComments.csv")
posts=post_data5$posts
comments=post_data5$comments

plot(posts,comments, col = "black", pch = 20)

plot(year,Comments_Per_Bronco_Post, col = "black", pch = 20)
points(year, yUser1, col = "red", pch = 20)
points(year, yBronco, col = "blue", pch = 20)
points(year, yUser3, col = "green", pch = 20)
points(year, yUser4, col = "yellow", pch = 20)
points(year, yUser5, col = "purple", pch = 20)


#points(x, y2, col = "red", pch = 20)


##post_data$year=as.POSIXct(post_data$year, format="%Y", tz="")
#p=ggplot(post_data, aes(x = year, y =rate)) +


post_data1=read.csv("participationRate_1.csv")
post_data2=read.csv("participationRate_2.csv")
post_data3=read.csv("participationRate_3.csv")
post_data4=read.csv("participationRate_4.csv")
post_data5=read.csv("participationRate_5.csv")
#FILE.write("date,comment\n")
#post_data=read.csv("plot_conversationRateVXM.csv")
#post_data$year=as.POSIXct(post_data$year, format="%Y", tz="")
p=ggplot(post_data, aes(x = year, y =rate)) + 
  #geom_line(size=1.5)+ 
  #geom_point(alpha=0.20, colour="#489C79", size=2) +
  geom_point(colour="#8899cc", size=4) +
  xlab('') + ylab('Num. Comments Per Bronco Post')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)





# plot of 1. top ten list
#post_data=read.csv("gente.csv")
#post_data=read.csv("CBE.csv")
post_data=read.csv("participationRateBronco.csv")
#FILE.write("date,comment\n")
#post_data=read.csv("plot_conversationRateVXM.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")
p=ggplot(post_data, aes(x = day, y =pRate)) + 
  geom_line(size=1.5)+ 
  #geom_point(alpha=0.20, colour="#489C79", size=2) +
  #geom_point(colour="#8899cc", size=2) +
  xlab('') + ylab('Num. Comments Per Bronco Post')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)

#post_data=read.csv("postsDays.csv")
post_data=read.csv("CBE.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")
p=ggplot(post_data, aes(x =day, y =pRate)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('') + ylab('Num. Comments Per Bronco Post')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)





#dataPoints=read.csv("postsUsersWithInteractionsAll.csv")
dataPoints=read.csv("postsUsersWithInteractions3_loss.csv")
#plot(0:23, d, type='b', axes=FALSE)
#axis(side=1, at=c(0:23))
#axis(side=2, at=seq(0, 600, by=100))
#box()

dataPoints$color
dataPoints$Num_Posts
dataPoints$Num_Inter
p=ggplot(dataPoints, aes(x=Num_Posts,y=Num_Inter, axes=FALSE)) + 
  #geom_point(alpha=1,size =dataPoints$Size, colour="black", fill ="#EB6841", shape=21) + 
  #geom_point(size =dataPoints$Size, colour="black", fill ="#489C79",shape=21) + 
  #xlab('Num. Tweets') + ylab('Num. Interactions Recieved')+
  xlab('Num. Tweets') + ylab('')+
  xlim(0,30)+ylim(0,10)
p+theme(axis.text=element_text(size=13),
        axis.title=element_text(size=13,face="bold"))
(p)

# Sample data
df <- read.table(header=T, text='
  cond xval yval
     A    1  2.0
     A    2  2.5
     B    1  3.0
     B    2  2.0
')


library(ggplot2)

# Plot with standard lines and points
# group = cond tells it which points to connect with lines
ggplot(df, aes(x=xval, y=yval, group = cond)) +
  geom_line() +
  geom_point()



library(ggplot2)
library(scales)

dataPoints=read.csv("correlationsForR2.csv")
dataPoints$color
dataPoints$x
dataPoints$y
p=ggplot(dataPoints, aes(x=x,y=y, axes=FALSE))  
  geom_point(alpha=1,colour="black", fill ="#EB6841", shape=21) + 
 # geom_point(size =3, colour="black", fill ="#489C79",shape=21) + 
  xlab('Num. Tweets') + ylab('Num. Interactions Recieved')+
  #xlab('Num. Tweets') + ylab('')+
  #xlim(0,30)+ylim(0,10)
#p+theme(axis.text=element_text(size=13),
 #       axis.title=element_text(size=13,face="bold"))
(p)

dataPoints=read.csv("correlationsForR4.csv")
#mya <- data.frame(a=1:100)
dataPoints=read.csv("correlationsForR2.csv")
ggplot() +
  #geom_path(data=mya, aes(x=a, y=a, colour=2, size=seq(0.1,10,0.1))) +
  geom_point(data=dataPoints, aes(x=x, y=y, colour=color, size=3)) 
  #theme_bw() +
  #theme(text=element_text(size=11))

dataPoints=read.csv("correlationsForR4.csv")
#mya <- data.frame(a=1:100)
dataPoints=read.csv("lineRatings.csv")
ggplot() +
  #geom_path(data=mya, aes(x=a, y=a, colour=2, size=seq(0.1,10,0.1))) +
  geom_point(data=dataPoints, aes(x=x, y=y, size=3)) 
#theme_bw() +
#theme(text=element_text(size=11))



library(ggplot2)
library(reshape2)
dataPoints=read.csv("postsUsersWithInteractionsAll.csv")
dataPoints$color
p=ggplot(dataPoints,aes(x=Num_Posts,y=Num_Favs,colour=color)) + geom_line()+
  theme_set(theme_minimal())+
  xlab('') + ylab('Num. of Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))

library(ggplot2)
library(reshape2)
#postsUsersWithInteractionsAll.csv
# most mentioned actors comments
#Bot, Num. Replies Per Bot Tweet
#fig5a <- read.csv("numUniqueUsersBots.csv")
#fig5a <- read.csv("numParticipants2.csv")
#fig5a <- read.csv("forAnova.csv")
fig5a <- read.csv("anova.csv")
#Bot, Number_Replies_Per_Bot_Tweet
#fig5a <- read.csv("ParticipationRate.csv")
#Num._Interactions_Per_Bot_Tweet
#Bot, Percentage_Participants
#actor,value
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
#p <- ggplot(fig5a, aes(x =Bot, y =Num_Retweets_Per_Post)) + geom_bar(stat = "identity")  + theme_bw(base_size=25, base_family="Helvetica")
p <- ggplot(fig5a, aes(x =Bot, y =Percentage_Volunteers)) + geom_bar(stat = "identity")  + theme_bw(base_size=20, base_family="Helvetica")

(p)

fig5a <- read.csv("sources.csv")

library(ggplot2)
library(reshape2)
#fig5a <- read.csv("forAnova.csv")
fig5a <- read.csv("anova.csv")
#fig5a <- read.csv("anovaParticipants.csv")

#statlab@pstat.ucsb.edu
BotA <- 3
BotB <- 2
for (BotA in seq(2,5, by=1)) {
  for (BotB in seq(3,5, by=1)) {
    data <- fig5a[ ,c(1,BotA,BotB)]
    fig5a2 <- data.frame(tweet=rep(1:nrow(fig5a),ncol(fig5a)-1),
                         Bot=rep(colnames(data)[-1],each=241),
                         #fig5a2 <- data.frame(tweet=rep(1:49,4),Bot=rep(c("Bot1","Bot2","Bot3","Bot4"),each=49),
                         reply=c(fig5a[,BotA],fig5a[,BotB]))
    fig5a.aov <- aov(reply~Bot+Error(tweet/Bot),data=fig5a2)
    print (c(BotA, BotB))
    print(summary(fig5a.aov))
  }
}


fig5a2 <- data.frame(tweet=rep(1:nrow(fig5a), 4),
                     Bot=rep(colnames(fig5a)[-1],each=241),
                     #fig5a2 <- data.frame(tweet=rep(1:49,4),Bot=rep(c("Bot1","Bot2","Bot3","Bot4"),each=49),
                     reply=c(fig5a[,2],fig5a[,3], fig5a[,4],fig5a[,5]))
fig5a.aov <- aov(reply~Bot+Error(tweet/Bot),data=fig5a2)
summary(fig5a.aov)

library(ggplot2)
library(reshape2)
#fig5a <- read.csv("forAnova.csv")
#fig5a <- read.csv("anova.csv")
fig5a <- read.csv("anovaParticipants.csv")

#statlab@pstat.ucsb.edu
BotA <- 3
BotB <- 2
for (BotA in seq(2,5, by=1)) {
  for (BotB in seq(3,5, by=1)) {
    data <- fig5a[ ,c(1,BotA,BotB)]
    fig5a2 <- data.frame(tweet=rep(1:nrow(fig5a),ncol(fig5a)-1),
                         #Bot=rep(colnames(data)[-1],each=241),
                         Bot=rep(colnames(data)[-1],each=94),
                         #fig5a2 <- data.frame(tweet=rep(1:49,4),Bot=rep(c("Bot1","Bot2","Bot3","Bot4"),each=49),
                         reply=c(fig5a[,BotA],fig5a[,BotB]))
    fig5a.aov <- aov(reply~Bot+Error(tweet/Bot),data=fig5a2)
    print (c(BotA, BotB))
    print(summary(fig5a.aov))
  }
}



fig5a2 <- data.frame(tweet=rep(1:nrow(fig5a), 4),
                     Bot=rep(colnames(fig5a)[-1],each=94),
                     #fig5a2 <- data.frame(tweet=rep(1:49,4),Bot=rep(c("Bot1","Bot2","Bot3","Bot4"),each=49),
                     reply=c(fig5a[,2],fig5a[,3], fig5a[,4],fig5a[,5]))
fig5a.aov <- aov(reply~Bot+Error(tweet/Bot),data=fig5a2)
summary(fig5a.aov)





#Ran an anova test and found P value is significatly small (P=1.24e-05)
#Which means that there is a significant difference in the strategies selected. 
#We also ran a pairwise comparisons and found that those tests had significantly small 
#p value, showing that there is significant difference between all the startegies. 
#
#p <- ggplot(fig5a, aes(x =source, y =percentage)) + geom_bar(stat = "identity")  +coord_flip()+ theme_bw(base_size=20, base_family="Helvetica")



library(ggplot2)
library(reshape2)
#fig5a <- read.csv("forAnova.csv")
#fig5a <- read.csv("anova.csv")
fig5a <- read.csv("anovaParInter.csv")
#fig5a <- read.csv("anovaInteractions.csv")

#statlab@pstat.ucsb.edu
BotA <- 3
BotB <- 2
for (BotA in seq(2,5, by=1)) {
  for (BotB in seq(3,5, by=1)) {
    data <- fig5a[ ,c(1,BotA,BotB)]
    fig5a2 <- data.frame(tweet=rep(1:nrow(fig5a),ncol(fig5a)-1),
                         #Bot=rep(colnames(data)[-1],each=241),
                         Bot=rep(colnames(data)[-1],each=356),
                         #fig5a2 <- data.frame(tweet=rep(1:49,4),Bot=rep(c("Bot1","Bot2","Bot3","Bot4"),each=49),
                         reply=c(fig5a[,BotA],fig5a[,BotB]))
    fig5a.aov <- aov(reply~Bot+Error(tweet/Bot),data=fig5a2)
    print (c(BotA, BotB))
    print(summary(fig5a.aov))
  }
}



fig5a2 <- data.frame(tweet=rep(1:nrow(fig5a), 4),
                     Bot=rep(colnames(fig5a)[-1],each=356),
                     #fig5a2 <- data.frame(tweet=rep(1:49,4),Bot=rep(c("Bot1","Bot2","Bot3","Bot4"),each=49),
                     reply=c(fig5a[,2],fig5a[,3], fig5a[,4],fig5a[,5]))
fig5a.aov <- aov(reply~Bot+Error(tweet/Bot),data=fig5a2)
summary(fig5a.aov)





#Ran an anova test and observed a P value less than 0.001
#Which means that there is a significant difference in the strategies selected. 
#We also ran a pairwise comparisons and found that those tests had significantly small 
#p value, showing that there is significant difference between all the startegies. 
#
#p <- ggplot(fig5a, aes(x =source, y =percentage)) + geom_bar(stat = "identity")  +coord_flip()+ theme_bw(base_size=20, base_family="Helvetica")






#(p)
#sources.csv

contentAnova=aov(Percentage_Participants~Bot,data=fig5a)
anova(contentAnova)
#repeatedMeasureAnova
glm=glm(I(Percentage_Participants/100)~Bot,data=fig5a,family=binomial)
summary(glm)
#histogramBotGroups_direct.csv

library(ggplot2)
library(reshape2)
# most mentioned actors comments
fig5a <- read.csv("histogramBotGroups_solidarity.csv")
#actor,value
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x =messages, y =percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)


library(ggplot2)
library(reshape2)
# most mentioned actors comments
#fig5a <- read.csv("sourceMG.csv")
#fig5a <- read.csv("source2_dcabellor_top.csv")
#fig5a <- read.csv("sourcesMinorias_dcabellor_top.csv")
#fig5a <- read.csv("sourcesMinorias_hcapriles_top.csv")
#fig5a <- read.csv("source2_hcapriles_top.csv")
#luislopezpsuv
#source2_nicolasmaduro_top.csv
fig5a <- read.csv("sourcesMinorias_tareckpsuv_top.csv")
#source2_leopoldolopez_top.csv
#source2_hcapriles_top.csv
#sourcesMinorias_hcapriles_top.csv
#sourcesMinorias_dcabellor_top.csv
#source2_dcabellor_top.csv
#actor,value
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x =Platform, y =Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)



#dailyPostsVXT.csv
#day, numPosts
post_data=read.csv("postsDays.csv")
#post_data=read.csv("dailyPostsVXT.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")

p=ggplot(post_data, aes(x =day, y =numPosts)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('') + ylab('Number of Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)



# plot of 1. top ten list
#post_data=read.csv("gente.csv")
post_data=read.csv("1User1.csv")
#post_data=read.csv("plot_conversationRateVXM.csv")
post_data$date=as.POSIXct(post_data$date, format="%Y-%m-%d", tz="")
p=ggplot(post_data, aes(x = date, y =value)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour=post_data$color, size=1) +
  xlab('Day') + ylab('Replies Per Admin Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)




#lycel

library(ggplot2)
library(reshape2)

dataPoints=read.csv("daynNight.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
dataPoints$color
p=ggplot(dataPoints,aes(x=date,y=time,colour=Type,group=color)) + geom_line()+
theme_set(theme_minimal())+
xlab('') + ylab('Num. of Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
        
(p)


#graph 1
dataPoints=read.csv("1User7.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
dataPoints$color
p=ggplot(dataPoints,aes(x=date,y=value)) + geom_line()+
  theme_set(theme_minimal())+
  xlab('') + ylab('')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))

(p)

#actor mentions
post_dataTemplarios=read.csv("actorMentionsParticipations_templarios.csv")
post_dataGente=read.csv("actorMentionsParticipations_gente.csv")
post_dataGoyo=read.csv("actorMentionsParticipations_goyo2.csv")
post_dataAutodefensa=read.csv("actorMentionsParticipations_autodefensa.csv")
#post_dataGoyo=read.csv("actorMentions_goyo.csv")
post_dataGobierno=read.csv("actorMentionsParticipations_gobierno.csv")
#post_dataTemplarios$date=as.POSIXct(post_data$date, format="%Y-%m-%d", tz="")

#ACTORS
post_dataTemplarios$date=as.POSIXct(post_dataTemplarios$date, format="%Y-%m-%d", tz="")
p=ggplot(post_dataTemplarios, aes(date)) + 
  geom_point(aes(y=post_dataTemplarios$numMentions,size=post_dataTemplarios$participate,colour="templarios")) +
  geom_point(aes(y=post_dataGente$numMentions,size=post_dataGente$participate,colour="gente")) +
  geom_point(aes(y=post_dataGoyo$numMentions,size=post_dataGoyo$participate,colour=post_dataGoyo$color)) +
  # geom_point(aes(y=post_dataGobierno$numMentions,size=post_dataGobierno$participate,colour="gobierno")) +
  geom_point(aes(y=post_dataAutodefensa$numMentions,size=post_dataAutodefensa$participate,colour="autodefensas")) +
  xlab('') + ylab('Interactions per Post')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))


(p)


# Fig 10
fig5a <- read.csv("municipiosScoreShort.csv")
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x = Municipio, y =Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)





# most mentioned actors comments
fig5a <- read.csv("MostMentionedAuthorsComments.csv")
#actor,value
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x = Actor, y =Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)

# most mentioned actors comments
fig5a <- read.csv("MostMentionedAuthorsPosts.csv")
#actor,value
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x = Actor, y =Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)





# Fig 5a
fig5a <- read.csv("postCategoriesPercentages.csv")
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x = Topic, y =Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)

# Fig 5a
fig5a <- read.csv("postCategoriesPercentages.csv")
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme_bw(base_size=25, base_family="Helvetica")
(p)


#postCategoriesWithRep.pdf
dataPoints=read.csv("datesCategoriesPosts2.csv")
#dataPoints2=read.csv("datesCategoriesREP.csv")
#dataPoints=read.csv("datesCategoriesJUZ.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
#dataPoints2$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")

p=ggplot(dataPoints, aes(x = date,y=value)) + 
  
  #geom_line(aes(y=value, colour=dataPoints$category))+ #geom_point(alpha=0.20, colour="red", size=1) +
 # geom_point(alpha=1, colour=dataPoints$category,size=3) +
  geom_point(alpha=1,colour=dataPoints$category,size =3, fill = NA, shape=21) + 
#  geom_point(alpha=1,colour=dataPoints$category,size =3, fill = NA, shape=21) + 
  #geom_line(aes(y=dataPoints2$value,colour=dataPoints2$category))+
 # geom_point(aes(y=dataPoints2$value,alpha=0,colour="white")) + 
  # geom_point(alpha=1, size=3,colour=dataPoints$category) + 
 # xlab('') + ylab('Percentage of Posts')
  xlab('') + ylab('')
#+ylim(0,3)
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
#p+ylim(0,3)

(p)

post_data=read.csv("plot_conversationRateVXM.csv")
#post_data=read.csv("actorMentions_gente.csv")
p=ggplot(post_data, aes(x = week, y = rate)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('Day') + ylab('Replies Per Admin Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)











#num one timers
dataPoints=read.csv("onetimeParticipants.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =numUsers)) +
  theme_set(theme_minimal())+
  geom_point(alpha=1,size =3, fill = NA, shape=21) + 
  xlab('') + ylab('Num. of New Participants')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#sizeCommentsWithPostsWithActors
dataPoints=read.csv("2.postsSCActores.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$sc)) + 
  theme_set(theme_minimal())+
  #p=ggplot(dataPoints, aes(x = date, y =dataPoints$participate)) +
  geom_point(alpha=.6, colour=dataPoints$actor,size=2, label=dataPoints$actor,fill = NA, shape=21) + 
  # geom_point(fill = NA, shape=21) + 
  #   geom_point(alpha=1,size =dataPoints$participate, colour=dataPoints$color, label=dataPoints$actor) + 
  #  geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  
  xlab('') + ylab('num. words in comments per post')
#p+theme_set(theme_minimal())
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#CommentsMentioningActors
dataPoints=read.csv("commentsPublicFigures.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$value)) + 
  theme_set(theme_minimal())+
 geom_point(alpha=.3, colour=dataPoints$color,size=4, label=dataPoints$color,fill =dataPoints$color, shape=21) + 
  xlab('') + ylab('Number of Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)



dataPointsHistogram=read.csv("plot_histogramLifetimes.csv")
names(dataPointsHistogram)
duration=dataPointsHistogram$week
g =qplot(week, data=dataPointsHistogram, binwidth =3,ylab = "Number of Accounts", xlab="Age Account in Number of Weeks", geom="histogram")
g+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))


#qplot(dataPointsHistogram, data=dataPointsHistogram$week, geom="histogram")
#duration=dataPointsHistogram$fre
#hist(dataPointsHistogram$week, breaks=12, col="red")
#duration = faithful$eruptions 
#hist(duration,    # apply the hist function 
 #    +   right=FALSE)    # intervals closed on the left
#hist(duration)

dataPoints=read.csv("plot_dataColors.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d %H:%M:%S", tz="")
#dataPoints$start=as.POSIXct(dataPoints$start, format="%Y-%m-%d %H:%M:%S", tz="")
dataPoints$color
p=ggplot(dataPoints, aes(x = day, y = age)) + 
  #geom_point(shape=1) +
  #dataPoints$color
  #eom_point(colour=dataPoints$color) + 
  #geom_point(alpha=0.3,size = .30, colour=dataPoints$color) + 
  geom_point(alpha=1,size =dataPoints$size, colour=dataPoints$color) + 
  #geom_point(alpha=0.20, colour="#7D851D") + 
  # scale_colour_gradient() +
  #scale_x_datetime(breaks = date_breaks("7 days"), labels = date_format("%m")) +
  xlab('') + ylab('Account Age Scale')
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
(p)








#reference,comment, size is based on likes
#CLThemselvesRef.png
#dataPoints=read.csv("CLAudience.csv")
#dataPoints=read.csv("CLThemselves.csv")
dataPoints=read.csv("CRThemselves.csv")
dataPoints$comment
p=ggplot(dataPoints, aes(x =reference, y = comment)) + 
  geom_point(alpha=1,size =dataPoints$likes, colour="black") + 
  #xlab('Number of References to Audience') + ylab('Number of Comments')
  xlab('Number of References to Themselves') + ylab('Number of Comments')
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
(p)







#CommentsLikesResharesGraph
#dataPoints=read.csv("commentLikeResharePost.csv")
#commentLikeResharePostAudienceReference.csv
#dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d %H:%M:%S", tz="")
#dataPoints=read.csv("CLRThemselves.csv")
#dataPoints=read.csv("CLRAudience.csv")
#dataPoints=read.csv("commentLikeResharePostThemReference.csv")
dataPoints=read.csv("CLAudience.csv")
#dataPoints$comment
p=ggplot(dataPoints, aes(x =refAudience, y = comment)) + 
  #geom_point(alpha=1,size =dataPoints$reshare, colour="black") + 
  geom_point(alpha=1,size =dataPoints$size, fill = NA, shape=21) + 
  #xlab('Num. of References to Themselves') + ylab('Num. of Comments')
  xlab('Number of References to Public') + ylab('Number of Comments')
  #xlab('Number of Comments') + ylab('Number of Likes')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)




#date,sizeMessage,sizeP
dataPoints=read.csv("dateSizeMessageNumPart.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x =date, y = sizeMessage)) + 
  geom_point(alpha=1,size =dataPoints$sizeP, fill = NA, shape=21) + 
  xlab('') + ylab('Number of Words')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)









#Message Size Date
post_data=read.csv("dateSizeMessage.csv")
post_data$date=as.POSIXct(post_data$date, format="%Y-%m-%d", tz="")
#date,sizeMessage
p=ggplot(post_data, aes(x = date, y = sizeMessage)) + 
  geom_line(size=1.5)+ geom_point(colour="black", size=1) +
  xlab('') + ylab('Num. of Words')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#sizeCommentsWithPostsWithActors
dataPoints=read.csv("2.postsSCActores.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$sc)) + 
  theme_set(theme_minimal())+
  #p=ggplot(dataPoints, aes(x = date, y =dataPoints$participate)) +
  geom_point(alpha=.6, colour=dataPoints$actor,size=2, label=dataPoints$actor,fill = NA, shape=21) + 
  # geom_point(fill = NA, shape=21) + 
  #   geom_point(alpha=1,size =dataPoints$participate, colour=dataPoints$color, label=dataPoints$actor) + 
  #  geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  
  xlab('') + ylab('num. words in comments per post')
#p+theme_set(theme_minimal())
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#NumCommentsMentionActors
dataPoints=read.csv("commentsPublicFigures.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$value)) + 
  theme_set(theme_minimal())+
 geom_point(alpha=.6,size=2, label=dataPoints$actor,fill = NA, shape=21) + 
  xlab('') + ylab('num. words in comments per post')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)




#

#lycel
dataPoints=read.csv("2.mentionsPopularity.csv")
#dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
dataPoints$color
p=ggplot(dataPoints, aes(x =mentions,y=participate)) +
  theme_set(theme_minimal())+
  geom_point(colour=dataPoints$color,size=10,alpha=1) + 
 # geom_point(colour=dataPoints$color,size=4, fill = NA, shape=21) + 
  xlab('Num. Posts') + ylab('Interactions per Posts')
p+theme(axis.text=element_text(size=25),
        axis.title=element_text(size=25,face="bold"))
(p)

# Fig 5a
fig5a <- read.csv("postCategoriesPercentages.csv")
# p <- ggplot(fig5a, aes(x = Category, y = Percentage, fill=Category)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=20))
# p <- ggplot(fig5a, aes(x = Category, y = Percentage)) + geom_bar(stat = "identity") + coord_flip() + theme(text = element_text(size=25))
p <- ggplot(fig5a, aes(x = Topic, y =Percentage)) + 
  geom_bar(stat = "identity")# + coord_flip()
#theme(text = element_text(size=20)
p+theme(axis.text=element_text(size=25,angle = 90),
        axis.title=element_text(size=25,face="bold"),legend.text=element_text(size=25,face="bold"))
 # coord_flip() + theme(size=25,face="bold")
(p)
#p+theme(axis.text=element_text(size=25),
#axis.title=element_text(size=25,face="bold"))

#lycel
#actorMentionsParticipationsAll3.csv
dataPoints=read.csv("actorMentionsParticipationsAll3.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
dataPoints$color
p=ggplot(dataPoints, aes(x = date,y =dataPoints$mentions)) +
  theme_set(theme_minimal())+
  geom_point(alpha=.7,size =3, colour=dataPoints$color, label=dataPoints$actor) + 
  xlab('') + ylab('Num. of Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


dataPoints=read.csv("commentsPublicFigures.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
dataPoints$color
p=ggplot(dataPoints, aes(x = date,y =dataPoints$value)) +
  theme_set(theme_minimal())+
  geom_point(alpha=.7,size =3, colour=dataPoints$color, label=dataPoints$actor) + 
  xlab('') + ylab('Num. of Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)




#lycel
#dataPoints=read.csv("actorMentionsParticipations_goyo2.csv")
dataPoints=read.csv("actorMentionsParticipationsAll2.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
dataPoints$color
p=ggplot(dataPoints, aes(x = date,y =dataPoints$mentions)) +
#p=ggplot(dataPoints, aes(x = date,y =dataPoints$participate)) + 
  theme_set(theme_minimal())+
  #geom_point(alpha=1,size =1, fill = NA, shape=21) + 
#p=ggplot(dataPoints, aes(x = date, y =dataPoints$participate)) +
 # geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
 # geom_point(colour=dataPoints$color,size=dataPoints$size, fill = NA, shape=21) + 
  #geom_point(alpha=1, label=dataPoints$actor) + 
  #geom_point(colour=dataPoints$color,alpha=.5) +
  #geom_point(colour=dataPoints$color,size=dataPoints$size,alpha=.6) + 
 #geom_point(colour=dataPoints$color,size=4, fill = NA, shape=21) + 
   geom_point(alpha=.7,size =3, colour=dataPoints$color, label=dataPoints$actor) + 
#  geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  xlab('') + ylab('Num. of Posts')
 # xlab('') + ylab('')
 # xlab('') + ylab('Num. of Posts')
#p+theme_set(theme_minimal())
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#sizeCommentsWithPosts
dataPoints=read.csv("postsWithSizeComments_VXM.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$sc)) + 
  theme_set(theme_minimal())+
  #p=ggplot(dataPoints, aes(x = date, y =dataPoints$participate)) +
  # geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  geom_point(fill = NA, shape=21) + 
  #   geom_point(alpha=1,size =dataPoints$participate, colour=dataPoints$color, label=dataPoints$actor) + 
  #  geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  
  xlab('') + ylab('num. words in comments')
#p+theme_set(theme_minimal())
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)

#type of mention and start date
dataPoints=read.csv("contentCommentedSD.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$categoria)) + 
  theme_set(theme_minimal())+
  #p=ggplot(dataPoints, aes(x = date, y =dataPoints$participate)) +
  # geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  geom_point(fill = NA, shape=21,colour=dataPoints$color) + 
  #   geom_point(alpha=1,size =dataPoints$participate, colour=dataPoints$color, label=dataPoints$actor) + 
  #  geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  
  xlab('') + ylab('Avg. comments per post')
#p+theme_set(theme_minimal())
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)






#sizeCommentsWithPostsWithActors
dataPoints=read.csv("2.postsSCActores.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$sc)) + 
  theme_set(theme_minimal())+
  #p=ggplot(dataPoints, aes(x = date, y =dataPoints$participate)) +
   geom_point(alpha=1, colour=dataPoints$actor, label=dataPoints$actor,fill = NA, shape=21) + 
 # geom_point(fill = NA, shape=21) + 
  #   geom_point(alpha=1,size =dataPoints$participate, colour=dataPoints$color, label=dataPoints$actor) + 
  #  geom_point(alpha=1, colour=dataPoints$color, label=dataPoints$actor) + 
  
  xlab('') + ylab('num. words in comments')
#p+theme_set(theme_minimal())
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#number of comments and start date.
dataPoints=read.csv("usersStartDateSizeComments.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date,y =dataPoints$sizeComments)) + 
  theme_set(theme_minimal())+
  #geom_point(alpha=1, label=dataPoints$actor) + 
  geom_point(fill = NA, shape=21) +  
  xlab('Date of First Comment or Like') + ylab('num. words in comments')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


















#actor mentions
post_dataTemplarios=read.csv("actorMentions_templarios.csv")
post_dataTemplarios=read.csv("actorMentions_templarios.csv")
post_dataGente=read.csv("actorMentions_gente.csv")
post_dataAutodefensa=read.csv("actorMentions_autodefensa.csv")
post_dataGoyo=read.csv("actorMentions_goyo.csv")
post_dataGobierno=read.csv("actorMentions_gobierno.csv")
post_dataTemplarios$date=as.POSIXct(post_dataTemplarios$date, format="%Y-%m-%d", tz="")

#ACTORS
post_dataTemplarios$date=as.POSIXct(post_dataTemplarios$date, format="%Y-%m-%d", tz="")

p=ggplot(post_dataTemplarios, aes(date)) + 
  geom_point(aes(y=post_dataTemplarios$amount,alpha=1,color="black")) +
  geom_point(aes(y=post_dataGente$amount,alpha=1,colour="#B8DC3C")) +
  geom_point(aes(y=post_dataGoyo$amount,alpha=1,colour="#A31A48")) +
 # geom_point(aes(y=post_dataGobierno$amount,size=1,colour="#9BF0E9")) +
  geom_point(aes(y=post_dataAutodefensa$amount,alpha=1,colour="#EA3556")) +
  xlab('') + ylab('Num. Posts with Mentions')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#actor mentions
post_dataTemplarios=read.csv("actorMentionsParticipations_templarios.csv")
post_dataGente=read.csv("actorMentionsParticipations_gente.csv")
post_dataGoyo=read.csv("actorMentionsParticipations_goyo2.csv")
post_dataAutodefensa=read.csv("actorMentionsParticipations_autodefensa.csv")
#post_dataGoyo=read.csv("actorMentions_goyo.csv")
post_dataGobierno=read.csv("actorMentionsParticipations_gobierno.csv")
#post_dataTemplarios$date=as.POSIXct(post_data$date, format="%Y-%m-%d", tz="")

#ACTORS
post_dataTemplarios$date=as.POSIXct(post_dataTemplarios$date, format="%Y-%m-%d", tz="")
p=ggplot(post_dataTemplarios, aes(date)) + 
  geom_point(aes(y=post_dataTemplarios$numMentions,size=post_dataTemplarios$participate,colour="templarios")) +
  geom_point(aes(y=post_dataGente$numMentions,size=post_dataGente$participate,colour="gente")) +
  geom_point(aes(y=post_dataGoyo$numMentions,size=post_dataGoyo$participate,colour=post_dataGoyo$color)) +
 # geom_point(aes(y=post_dataGobierno$numMentions,size=post_dataGobierno$participate,colour="gobierno")) +
  geom_point(aes(y=post_dataAutodefensa$numMentions,size=post_dataAutodefensa$participate,colour="autodefensas")) +
  xlab('') + ylab('Interactions per Post')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))


(p)




p=ggplot(dataPoints, aes(x =date, y = sizeMessage)) + 
  geom_point(alpha=1,size =dataPoints$sizeP, fill = NA, shape=21) + 
  xlab('') + ylab('Number of Words')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)




p=ggplot(post_dataTemplarios, aes(date)) +
  geom_line(aes(y=post_dataTemplarios$amount, colour="templarios"))+

#actors
post_dataTemplarios=read.csv("actorMentions_templarios.csv")
post_dataGente=read.csv("actorMentions_gente.csv")
post_dataAutodefensa=read.csv("actorMentions_autodefensa.csv")
post_dataTemplarios$date=as.POSIXct(post_dataTemplarios$date, format="%Y-%m-%d", tz="")
p=ggplot(post_dataTemplarios, aes(date)) +
  geom_line(aes(y=post_dataTemplarios$amount, colour="templarios"))+
  geom_line(aes(y=post_dataGente$amount, colour="gente"))+
  geom_line(aes(y=post_dataAutodefensa$amount, colour="autodefensa"))+
  #geom_line(aes(y=post_dataAutodefensa$amount, colour="autodefensas"))+
  xlab('Day') + ylab('Num. of Mentions')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)

post_data=read.csv("plot_conversationRateVXM.csv")
p=ggplot(post_data, aes(x = week, y = rate)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('Day') + ylab('Replies Per Admin Posts')
p+theme(axis.text=element_text(size=15),
       axis.title=element_text(size=15,face="bold"))
(p)

#num replies author replies
post_data=read.csv("adminPostReplies.csv")
post_data$date=as.POSIXct(post_data$date, format="%Y-%m-%d", tz="")

p=ggplot(post_data, aes(x =date, y =value)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('Day') + ylab('Percentage of Posts Admin Replied')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)

#dailyPostsVXT.csv
post_data=read.csv("postsDays.csv")
#post_data=read.csv("dailyPostsVXT.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")

p=ggplot(post_data, aes(x =day, y =numPosts)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('') + ylab('Number of Posts')
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
(p)


post_data=read.csv("totalParticipationsDay.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")

p=ggplot(post_data, aes(x =day, y =value)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('') + ylab('Num. Participations per Post')
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
(p)

post_data=read.csv("postsDaysWithMedia.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")

p=ggplot(post_data, aes(x =day, y =numMedia)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('') + ylab('Media per Admin Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)

#Account Tenure vs join date
post_data=read.csv("tenuerStartDateDia.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")
p=ggplot(post_data, aes(x =day, y =age)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('') + ylab('Median Account Tenure')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


dataPoints=read.csv("tenuerStartDateDia.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =age)) + 
  geom_point(alpha=1,size =1, colour="black") + 
  xlab('') + ylab("Median Account Tenure")
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
(p)



dataPoints=read.csv("tenuerStartDateAll.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =age)) + 
  geom_point(alpha=1,size =1, colour="black") + 
  xlab('') + ylab("Median Account Tenure")
p+theme(axis.text=element_text(size=20),
        axis.title=element_text(size=20,face="bold"))
(p)






#Account Tenure vs join date
post_data=read.csv("participateAllStartDate.csv")
post_data$day=as.POSIXct(post_data$day, format="%Y-%m-%d", tz="")
p=ggplot(post_data, aes(x =day, y =participate)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('Day of First Comment or Like') + ylab('Number of Comments or Likes')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#comments-likes non One timers
#dataPoints=read.csv("SDLCNonOneTimers2.csv")
#dataPoints=read.csv("SDCLNon1Timers2.csv")
dataPoints=read.csv("SDLCNon1Timers2.csv")
#dataPoints=read.csv("SDCLNonOneTimers.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =likes)) + 
  geom_point(alpha=1,size =3, fill = NA, shape=21) + 
  #p=ggplot(dataPoints, aes(x = day, y =comments)) + 
 # geom_point(alpha=1,size =dataPoints$comments, fill = NA, shape=21) + 
 # geom_point(alpha=1,size =dataPoints$likes, fill = NA, shape=21) + 
  xlab('Day of First Participation') + ylab('Num. of Participations')
 # xlab('Day of First Comment') + ylab('Num. Comments')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)



dataPoints=read.csv("totalCommentsSD.csv")
dataPoints$date=as.POSIXct(dataPoints$date, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = date, y =numComments)) + 
  geom_point(alpha=1,size =3, fill = NA, shape=21) + 
  xlab('Day of First Participation') + ylab('Num. of Comments')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)














#Med Tenure & New PPL
dataPoints=read.csv("MedTenure&NewPPL.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =tenure)) +
  geom_point(alpha=1,size =dataPoints$joined, fill = NA, shape=21) + 
xlab('Day of First Like or Comment') + ylab('Median Account Tenure')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)



#partication of all users
dataPoints=read.csv("participateAllStartDate.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =participate)) +
  geom_point(alpha=1,size =2, fill = NA, shape=21) + 
  xlab('Day of First Comment or Likes') + ylab('Num. Comments and Likes')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#partication of all users & new people joining
dataPoints=read.csv("participate&NewPPL.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
p=ggplot(dataPoints, aes(x = day, y =participate)) +
  geom_point(alpha=1,size =dataPoints$newppl, fill = NA, shape=21) + 
  xlab('Day of First Comment or Like') + ylab('Num. Comments and Likes')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)


#boxplot account tenure join date
dataPoints=read.csv("tenureVarStartDate_VXM.csv")
dataPoints$day=as.POSIXct(dataPoints$day, format="%Y-%m-%d", tz="")
#ggplot(dataPoints, aes(x=day, y=age)) + geom_boxplot()

#dataPoints.long<-melt(dataPoints,id.vars="")
#ggplot(df.long,aes(month,value))+geom_boxplot()
ggplot(dataPoints, aes(day, age)) +geom_boxplot()
  #geom_point(aes(color = age))
(p)

#df$month<-factor(month.name,levels=month.name)
#library(reshape2)






post_data=read.csv("plot_conversationRateVXM.csv")
p=ggplot(post_data, aes(x = week, y = rate)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('Day') + ylab('Replies Per Admin Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)

X <-post_data$week
Y <-post_data$rate
labelsT<-post_data$date
p=ggplot(post_data, aes(x = week, y = rate, label=labelsT, angle=45)) + 
 # label = x,angle=45
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1,label=labelsT, angle=45) +
  xlab('Day') + ylab('Replies Per Admin Posts')


p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))

(p)
df <- data.frame(X, Y)


p <- ggplot(data=df, aes(x = X,y = Y) )
p <- p + labels=c(ticks)
p <- p + geom_point()
p <- p + theme_bw()
p




post_data=read.csv("plot_reshareRateVXM.csv")
p=ggplot(post_data, aes(x = week, y = rate)) + 
  geom_line(size=1.5)+ geom_point(alpha=0.20, colour="black", size=1) +
  xlab('Day') + ylab('Reshares Per Admin Posts')
p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"))
(p)





post_data <- read.csv("plot_data.csv")
post_data$day <- as.POSIXct(post_data$day, format="%Y-%m-%d %H:%M:%S", tz="")
p <- ggplot(post_data, aes(x = day, y = age)) + 
  #geom_point(shape=1) +
  geom_point(alpha=0.20, colour="black") + 
  # scale_colour_gradient() +
  #scale_x_datetime(breaks = date_breaks("7 days"), labels = date_format("%m")) +
  xlab('Time') + ylab('Age scale')
(p)

# get data
#dat <- read.table(text = "Chr NonSyn_Snps Total_exonic_Snps
#A01 9217    13725
 #                 A02 6226    9133
  #                A03 14888   21531
  #                A04 5272    7482
  #                A05 4489    6608
   #               A06 8298    12212
  #                A07 6351    9368
  #                A08 3737    5592
  #                A09 12429   18119
   #               A10 7165    10525", header= TRUE)

#dat <- read.table(text = "Chr NonSyn_Snps Total_exonic_Snps
#A01 9217    13725
 #                 A02 6226    9133
  #                A03 14888   21531
  #                A04 5272    7482
  #                A05 4489    6608
   #               A06 8298    12212
  #                A07 6351    9368
  #                A08 3737    5592
  #                A09 12429   18119
   #               A10 7165    10525", header= TRUE)

dat <- read.table(text = "Chr Returning_Accounts New_Accounts
A01 0 390
A02 175 396
A03 144 151
                  A04 173 225
                  A05 204 228
                  A06 251 514
                  A07 258 309
                  A08 92 49
                  A09 117 79
                  A010 168 120
                  A011 171 159
                  A012 287 506
                  A013 292 370
                  A014 276 212
                  A015 219 143
                  A016 851 855
                  A017 884 964
                  A018 289 254
                  A019 240 156
                  A020 257 166
                  A021 227 153
                  A022 214 145
                  A023 184 125
                  A024 904 853
                  A025 1266 1484
                  A026 3339 6108
                  A027 2124 2105
                  A028 1312 1141
                  A029 1337 991
                  A030 1948 1648
                  A031 847 658
                  A032 1265 914
                  A033 832 655
                  A034 1144 817
                  A035 1959 1481
                  A036 1373 912
                  A037 1168 824
                  A038 964 658
                  A039 2065 800
                  A040 1144 817
                  A041 1959 1481
                  A042 1373 912
                  A043 1168 824
                  A044 964 658
                  A045 2065 800
                  
                  ", header= TRUE)

post_data <- read.csv("plot_numReturningNewUsers.csv")
# load libraries
require(ggplot2)
require(reshape2)
# melt data from wide to long
dat_m <- melt(dat)

# plot
p=ggplot(dat_m, aes(Chr, value, fill = variable)) + 
  geom_bar(stat = "identity") + 
  xlab("") + 
  ylab("Num. of Participants")
p=p+theme_set(theme_minimal())
p=p + theme(axis.text.x = element_text(angle = 90, hjust = 1, size=1,color="darkred"))

p+theme(axis.text=element_text(size=15),
        axis.title=element_text(size=15,face="bold"),
        legend.text = element_text(colour = 'black', size = 10, face = 'bold'))

