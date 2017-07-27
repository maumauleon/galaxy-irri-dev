##########################################################
##########################################################
#Function for do the AMMI model and SREG model with biplot and 3D plots
#Autor:Angela Pacheco
#R-version:3.2.0
##########################################################
##########################################################


AMMISREG<-function(datos=datos,analysis=analysis,ExpDes=ExpDes,BiplotFormat=BiplotFormat,traits=traits,selected=selected,LSMeans_par=LSMeans_par,plot3D=plot3D,polygoner=polygoner,tmp=tmp){
rm(list=ls(all=TRUE))
library(estimability)
library(lsmeans)
library(reshape)
library(nlme)
#library(rgl)

#####################################################
#Function for maintain open R in the 3D plot
#library(tcltk)
#library(tcltk2)
#mywait <- function() {
#  tt <- tktoplevel()
#  tkpack( tkbutton(tt, text='Continue', command=function()tkdestroy(tt)),
#          side='bottom')
#  tkbind(tt,'<Key>', function()tkdestroy(tt) )
#  tkwait.window(tt)
#}
#####################################################

orgdir=getwd()
index <- which(as.character(datos$Loc)%in%selected)
  if(length(index)>0)	datos <- datos[index,]
  
for (b in 1:length(traits)){ 
  
  if (ExpDes=="LSMeans"){
    lenv1=sort(levels(as.factor(datos$ENV)))
	lgen1=sort(levels(as.factor(datos$GEN)))
    datos$Entry=as.numeric(as.factor(datos$GEN))
    datos$Loc=as.numeric(as.factor(datos$ENV))
	nenv<-max(as.numeric(datos$Loc))
	ngen<-max(as.numeric(datos$Entry))
    raw=datos[order(datos$Loc,datos$Entry),c("Loc","Entry",traits[b])]
	varname=traits[b]
    colnames(raw)=c("ENV","GEN","YLD")
	raw$ENV=as.factor(raw$ENV)
	raw$GEN=as.factor(raw$GEN)
	raw$YLD=as.numeric(as.character(raw$YLD))	
	lenv1=lenv1[1:nenv]
	lgen1=lgen1[1:ngen]
  }
  
  if (ExpDes=="RCB"){
    lenv1=sort(levels(as.factor(datos$ENV)))
	lgen1=sort(levels(as.factor(datos$GEN)))
    datos$Entry=as.numeric(as.factor(datos$GEN))
    datos$Loc=as.numeric(as.factor(datos$ENV))
    datos$Rep=as.numeric(as.factor(datos$REP))
	nenv<-max(as.numeric(datos$Loc))
	ngen<-max(as.numeric(datos$Entry))
	nrep<-max(as.numeric(datos$Rep))
	raw=datos[order(datos$Loc,datos$Entry,datos$Rep),c("Loc","Entry","Rep",traits[b])]
    varname=traits[b]
    colnames(raw)=c("ENV","GEN","REP","YLD")
	raw$ENV=as.factor(raw$ENV)
	raw$GEN=as.factor(raw$GEN)
	raw$REP=as.factor(raw$REP)
	raw$YLD=as.numeric(as.character(raw$YLD))
    lenv1=lenv1[1:nenv]
	lgen1=lgen1[1:ngen]	
  }

  
  if (ExpDes=="Lattice"){
    lenv1=sort(levels(as.factor(datos$ENV)))
	lgen1=sort(levels(as.factor(datos$GEN)))
    datos$Entry=as.numeric(as.factor(datos$GEN))
    datos$Loc=as.numeric(as.factor(datos$ENV))
    datos$Rep=as.numeric(as.factor(datos$REP))
	datos$Block=as.numeric(as.factor(datos$BLOCK))
	nenv<-max(as.numeric(datos$Loc))
	ngen<-max(as.numeric(datos$Entry))
	nrep<-max(as.numeric(datos$Rep))
    raw=datos[order(datos$Loc,datos$Entry,datos$Rep,datos$Block),c("Loc","Entry","Rep","Block",traits[b])]
    varname=traits[b]
	colnames(raw)=c("ENV","GEN","REP","BLOCK","YLD")
	raw$ENV=as.factor(raw$ENV)
	raw$GEN=as.factor(raw$GEN)
	raw$REP=as.factor(raw$REP)
	raw$BLOCK=as.factor(raw$BLOCK)    
	raw$YLD=as.numeric(as.character(raw$YLD))	
	lenv1=lenv1[1:nenv]
	lgen1=lgen1[1:ngen]
    }
  
  if (ExpDes=="RCB"){
    
	gtest=anova(lm(YLD ~ ENV+GEN+ENV*GEN,data=raw,na.action=na.omit ))
    #Analysis of Varianza Using All Data
    ver=anova(lm(YLD ~ REP+ENV+GEN+ENV*GEN,data=raw,na.action=na.omit ))
    
    ammi=lm(YLD ~ REP+ENV+GEN,data=raw,na.action=na.omit )
    sreg=lm(YLD ~ REP+ENV,data=raw,na.action=na.omit )
    multmod=lm(YLD ~ REP,data=raw,na.action=na.omit )
    
    if (analysis=="AMMI"){res=ammi$residuals}
    if (analysis=="SREG"){res=sreg$residuals}
    if (analysis=="MULTMOD"){res=multmod$residuals}
    
    res=as.data.frame(cbind(raw$GEN,raw$ENV,raw$REP,res))
    colnames(res)=c("GEN","ENV","REP","RESIDUAL")
    
    outres=cast(res,GEN~ENV,mean,value="RESIDUAL")
    #outres$GEN=as.character(outres$GEN)
    #outres2=outres[order(outres$GEN),]
	outres2=outres
    
    msem=ver[5,2]/ver[5,1]
    dfem=ver[5,1]
    
    nrep=length(levels(raw$REP))
  }
  
  if (ExpDes=="Lattice"){
  
    gtest=anova(lm(YLD ~ ENV+GEN+ENV*GEN,data=raw,na.action=na.omit ))
    #namesorig=levels(raw$ENV)
    #raw$ENV=as.factor(as.numeric(raw$ENV))
    #nameafter=levels(raw$ENV)
    covparms=list()
    lsgen=list()
    test=list()
    
    for (i in 1:length(levels(raw$ENV))){
      raw2<<-raw[raw$ENV==levels(raw$ENV)[i],]
      ver=lme(YLD ~ REP+GEN,data=raw2,random=~ 1|BLOCK/REP,na.action=na.omit)  
      covparms[[i]]=cbind(c(levels(raw$ENV)[i]),c("residual"),round(as.numeric(VarCorr(ver)[5,1]),5))	  
      lsgen[[i]]=cbind(ENV=rep(levels(raw$ENV)[i],length(levels(raw$GEN))),as.matrix(summary(lsmeans(ver,"GEN")))[,1:2])
      test[[i]]=cbind(ENV=c(levels(raw$ENV)[i]),anova(ver)[3,2])
    }
    
    covparmsg=covparms[[1]]
    lsgeng=lsgen[[1]]
    testg=test[[1]]
    for (i in 2:length(levels(raw$ENV))){
      covparmsg=rbind(covparmsg,covparms[[i]])
      lsgeng=rbind(lsgeng,lsgen[[i]])
      testg=rbind(testg,test[[i]])
    }
    
    #MSE & DFE for the Gollob's Test
    msem=round(mean(as.numeric(covparmsg[,3])),5)
    dfem=sum(as.numeric(testg[,2]))
    #Adjusted Means Using Proc Mixed for AMMI
    meansa=as.data.frame(cbind(as.numeric(lsgeng[,1]),rep(order(as.character(1:ngen)),nenv),as.numeric(lsgeng[,3])))
	colnames(meansa)=c("ENV","GEN","YLD")
    meansa$ENV=as.factor(as.character(meansa$ENV))
    meansa$GEN=as.factor(as.character(meansa$GEN))
    #meansa=meansa[order(meansa$ENV,meansa$GEN),]
    
    
    ammi=lm(YLD ~ ENV+GEN,data=meansa,na.action=na.omit)
    sreg=lm(YLD ~ ENV,data=meansa,na.action=na.omit)
    
    if (analysis=="AMMI"){res=ammi$residuals}
    if (analysis=="SREG"){res=sreg$residuals}
    
    res=as.data.frame(cbind(meansa[,1:2],round(res,5)))
	colnames(res)=c("ENV","GEN","RESIDUAL")
    res$RESIDUAL=as.numeric(as.character(res$RESIDUAL))
	
    outres=cast(res,GEN~ENV,mean,value="RESIDUAL",na.rm=T)
	
	outres15=outres[,-1]
    outres15=outres15[,order(as.numeric(colnames(outres15)))]
	outres=cbind(GEN=outres$GEN,outres15)
	#outres$GEN=as.character(outres$GEN)
    #outres2=outres[order(outres$GEN),]
	outres2=outres
	#nrep=length(levels(raw$REP))
  }
  
  if (ExpDes=="LSMeans"){
  
    gtest=anova(lm(YLD ~ ENV+GEN+ENV*GEN,data=raw,na.action=na.omit ))
    #Analysis of Varianza Using All Data
    ver=anova(lm(YLD ~ ENV+GEN+ENV*GEN,data=raw,na.action=na.omit ))
    
    ammi=lm(YLD ~ ENV+GEN,data=raw,na.action=na.omit )
    sreg=lm(YLD ~ ENV,data=raw,na.action=na.omit )
    
    if (analysis=="AMMI"){res=ammi$residuals}
    if (analysis=="SREG"){res=sreg$residuals}
    
    res=as.data.frame(cbind(raw$GEN,raw$ENV,res))
    colnames(res)=c("GEN","ENV","RESIDUAL")
    
    outres=cast(res,GEN~ENV,mean,value="RESIDUAL")
    #outres$GEN=as.character(outres$GEN)
    #outres2=outres[order(outres$GEN),]
    outres2=outres
      msem<- LSMeans_par[1]
      dfem<- LSMeans_par[2]
      nrep<- LSMeans_par[3]
  }
  
  ##COMUN for both design
  #ngen=length(levels(raw$GEN))
  #nenv=length(levels(raw$ENV))
  
  outres3=as.matrix(as.matrix(outres2[,-1]))
  rownames(outres3)=outres2[,1]
  colnames(outres3)=colnames(outres2)[-1]
  outres4=sweep(outres3, 2, colMeans(outres3), "-")
  descpct=svd(outres4)
  
  #ver=round(det(var(outres2[,-1])),6)
  #if (analysis=="AMMI"& ver<=0){
  #descpct$v=svd(var(outres2[,-1])+diag(0.7,dim(outres2[,-1])[2]))$u
  #descpct$u=svd(tcrossprod(outres3))$u
  #}
  
  MINIMO=min(ngen,nenv)
  L=descpct$d[1:MINIMO]
  
  SS=(L**2)*nrep                     
  SUMA=sum(SS)
  PORCENT=((1/SUMA)*SS)*100
  
  PORCENAC=rep(1,MINIMO)
  DFA=rep(1,MINIMO)
  
  DFA[1]=(ngen-1)+(nenv-1)-(2*1-1)
  PORCENAC[1]=PORCENT[1]            
  
  for (i in 2:MINIMO){
    DFA[i]=(ngen-1)+(nenv-1)-(2*i-1)
    PORCENAC[i]=PORCENAC[i-1]+PORCENT[i]            
  }
  
  DFE=rep(dfem,MINIMO)
  MSE=rep(msem,MINIMO)
  SSDF=cbind(SS,PORCENT,PORCENAC,DFA,DFE,MSE)
  
  L12=L**0.5                         
  
  
  #descpct$u=-1*descpct$u ##es necesario porque en SAS los signos son contrarios
  #descpct$v=-1*descpct$v
  
  #if(analysis=="SREG" & ver<=0){
  #descpct$u[,1]=-1*descpct$u[,1] 
  #descpct$v[,1]=-1*descpct$v[,1]
  # }
  
  SCOREG1=descpct$u[,1]*L12[1]
  SCOREG2=descpct$u[,2]*L12[2]
  if(nenv>2) SCOREG3=descpct$u[,3]*L12[3]
  SCOREE1=descpct$v[,1]*L12[1]
  SCOREE2=descpct$v[,2]*L12[2]
  if(nenv>2) SCOREE3=descpct$v[,3]*L12[3]
  
  
  FACTOR1=max(cbind(abs(SCOREG1),abs(SCOREG2)))
  FACTOR2=max(cbind(abs(SCOREE1),abs(SCOREE2)))
  FACTOR=max(FACTOR1,FACTOR2)
  
  if(nenv>2) {
  SCOREG=cbind(SCOREG1,SCOREG2,SCOREG3)*(1/FACTOR1)
  SCOREE=cbind(SCOREE1,SCOREE2,SCOREE3)*(1/FACTOR2)
  }
  
  if(nenv==2) {
  SCOREG=cbind(SCOREG1,SCOREG2)*(1/FACTOR1)
  SCOREE=cbind(SCOREE1,SCOREE2)*(1/FACTOR2)
  }
  
  SCORES=rbind(SCOREG,SCOREE)
  
  
  PERC1=round(PORCENT[1],2)
  PERC2=round(PORCENT[2],2)
  if(nenv>2) PERC3=round(PORCENT[3],2)
  
  MSAMMI=round(SSDF[,1]/SSDF[,4],5)
  F_AMMI=round(MSAMMI/SSDF[,6],5)
  PROBF=round(1-pf(F_AMMI,SSDF[,4],DFE),5)
  
  PANOVA=as.matrix(c(gtest[1:3,2]*100/sum(as.matrix(gtest[1:3,2])),0))
  PPANOVA=as.matrix(c(PANOVA[1,],PANOVA[1,]+PANOVA[2,],PANOVA[1,]+PANOVA[2,]+PANOVA[3,],0))
  
  anovagollob=round(cbind(as.matrix(gtest[,2]),PANOVA ,PPANOVA ,as.matrix(gtest[,1]),as.matrix(gtest[,3]),as.matrix(gtest[,4]),as.matrix(gtest[,5])),5)
  #Gollobs Test for the AMMI factors
  GollobsCP=round(cbind(SS=SSDF[,1],PORCENT,PORCENAC,DF=DFA,MS=MSAMMI,F=F_AMMI,PROBF),5)
  Gollobs=as.matrix(rbind(anovagollob[1:3,],GollobsCP,anovagollob[4,]))
  
  cp=matrix("NA",1,dim(GollobsCP)[1])
   for(i in 1:dim(GollobsCP)[1]){
    cp[i]=paste("PC",i,sep="")
   }
  rownames(Gollobs)=c("ENV","GEN","ENV*GEN",cp,"Residuals")
  
  #* Starting the Biplot information ;
  #* For Obtaining the variables Type y Name for the Genotypes ;
  typegen=rep("GEN",ngen)
  gxe=cast(raw,GEN~ENV,mean,value="YLD")
  gxe$GEN=as.numeric(gxe$GEN)
  gxe=gxe[order(gxe$GEN),]
  yldgen=apply(gxe[,-1],1,mean,na.rm=T)
  namegen=lgen1
  
  
  
  #* For Obtaining the variables Type y Name for the Environments ;
  typenv=rep("ENV",nenv)
  yldenv=apply(gxe[,-1],2,mean,na.rm=T)
  nameenv=lenv1
  new3=cbind(nameenv,yldenv)
  #new3[,1]=as.character(new3[,1])
  #new3=new3[order(new3[,1]),]
  #Final Corrected Scores for Graphing the Biplot
  if (nenv>2){
  biplotdata=as.data.frame(cbind(rbind(cbind(typegen,namegen,yldgen),cbind(typenv,new3)),SCORES))
  colnames(biplotdata)=c("TYPE","NAME","YLD","DIM1","DIM2","DIM3")
  biplotdata$YLD=as.numeric(as.character(biplotdata$YLD))
  biplotdata$DIM1=as.numeric(as.character(biplotdata$DIM1))
  biplotdata$DIM2=as.numeric(as.character(biplotdata$DIM2))
  biplotdata$DIM3=as.numeric(as.character(biplotdata$DIM3))
  }
  
  if (nenv==2){
  biplotdata=as.data.frame(cbind(rbind(cbind(typegen,namegen,yldgen),cbind(typenv,new3)),SCORES))
  colnames(biplotdata)=c("TYPE","NAME","YLD","DIM1","DIM2")
  biplotdata$YLD=as.numeric(as.character(biplotdata$YLD))
  biplotdata$DIM1=as.numeric(as.character(biplotdata$DIM1))
  biplotdata$DIM2=as.numeric(as.character(biplotdata$DIM2))  
  }
  
  rownames(SCOREE)=new3[,1]
  rownames(SCOREG)=namegen   
  

  newfold=paste("Output&",paste(tmp,paste(analysis,paste(ExpDes,paste("&",traits[b],sep=""),sep=""),sep=""),sep=""),sep="")
  sal=paste(orgdir,paste("/",newfold,sep=""),sep="")
  dir.create(sal)
  setwd(sal)
  
  write.csv(Gollobs,paste("Gollobs test",paste(traits[b],paste(analysis,paste(ExpDes,".csv")))))
  write.csv(biplotdata,paste("Final Scores",paste(traits[b],paste(analysis,paste(ExpDes,".csv")))))
  ##Graphics
  
if (BiplotFormat=="pdf"){pdf(paste("Biplot PC1vsPC2",paste(traits[b],paste(ExpDes,paste(analysis,".pdf")))))}
if (BiplotFormat=="png"){png(paste("Biplot PC1vsPC2",paste(traits[b],paste(ExpDes,paste(analysis,".png")))))}
if (BiplotFormat=="wmf"){win.metafile(paste("Biplot PC1vsPC2",paste(traits[b],paste(ExpDes,paste(analysis,".wmf")))))}

  plot(SCOREE[,c(1,2)],type="n",main=paste(analysis,paste(varname,paste("from a",ExpDes))),
       xlab=paste("Factor 1",paste("(",paste(PERC1,"%)"))),
       ylab=paste("Factor 2",paste("(",paste(PERC2,"%)"))),cex=0.7,xlim=c(-1,1),ylim=c(-1,1),
       col.main=c("blue"),col.lab=c("blue"))
  text(SCOREG[,c(1,2)],col="blue",cex=0.7,labels=rownames(SCOREG))
  text(SCOREE[,c(1,2)],col="red",cex=0.7,labels=rownames(SCOREE))
  SCOREEa=SCOREE
  for (i in 1:dim(SCOREEa)[1]){
    if(SCOREEa[i,1]>0){SCOREEa[i,1]=SCOREEa[i,1]-0.02}
    if(SCOREEa[i,1]<0){SCOREEa[i,1]=SCOREEa[i,1]+0.02}
  }
  arrows(rep(0,dim(SCOREEa)[1]),rep(0,dim(SCOREEa)[1]),SCOREEa[,1],SCOREE[,2],col="green",length=0.07)
  abline(h=0)
  abline(v=0)
  
  if (polygoner==TRUE){
  uno=biplotdata$DIM1[1:ngen]
  dos=biplotdata$DIM2[1:ngen] 
  hpts <- chull(x = uno, y = dos)
  d1=cbind(uno[hpts], dos[hpts])
  #d=d1[order(d1[,1],decreasing=F),]
  d=rbind(d1,d1[1,])
  xxx=t(t(rep(0,(nrow(d)-1))))
  yyy=t(t(rep(0,(nrow(d)-1))))
  ppp=matrix(c(0, 1,1 ,0),2,2)
  for (i in 1:(nrow(d)-1)){
  dd=d[i:(i+1),]
  if (dd[1,1]>dd[2,1]){ddd=ppp%*%dd}
  if (dd[1,1]<=dd[2,1]){ddd=dd}
  p=(ddd[2,2]-ddd[1,2])/(ddd[2,1]-ddd[1,1])
  if (p<0){ss=1}
  if (p>=0){ss=-1}
  r=tan(((180-90-abs((atan(p)*180)/3.14156))*3.14156)/180)*ss 
  aa=((ddd[1,2]+ddd[2,2])/2)-(p*(ddd[1,1]+ddd[2,1])/2)
  xx=aa/(r-p)
  if (abs(r)<1){xxx[i,]=1} 
  if (abs(r)>=1){xxx[i,]=1/abs(r)}
  if (xx<0){xxx[i,]=(-1)*xxx[i,]}
  if (xx>=0){xxx[i,]=xxx[i,]}
  yyy[i,]=xxx[i,]*r  
  }
  per=cbind(xxx,yyy)
  lines(d[,1], d[,2], col = "blue",lty=2)
  s1=t(t(rep(0,dim(per)[1])))
  segments(s1,s1,per[,1],per[,2],lty=2)
   }
dev.off()

if (nenv>2){   
if (BiplotFormat=="pdf"){pdf(paste("Biplot PC1vsPC3",paste(traits[b],paste(ExpDes,paste(analysis,".pdf")))))}
if (BiplotFormat=="png"){png(paste("Biplot PC1vsPC3",paste(traits[b],paste(ExpDes,paste(analysis,".png")))))}
if (BiplotFormat=="wmf"){win.metafile(paste("Biplot PC1vsPC3",paste(traits[b],paste(ExpDes,paste(analysis,".wmf")))))}

plot(SCOREE[,c(1,3)],type="n",main=paste(analysis,paste(varname,paste("from a",ExpDes))),
     xlab=paste("Factor 1",paste("(",paste(PERC1,"%)"))),
     ylab=paste("Factor 3",paste("(",paste(PERC3,"%)"))),cex=0.7,xlim=c(-1,1),ylim=c(-1,1),
     col.main=c("blue"),col.lab=c("blue"))
text(SCOREG[,c(1,3)],col="blue",cex=0.7,labels=rownames(SCOREG))
text(SCOREE[,c(1,3)],col="red",cex=0.7,labels=rownames(SCOREE))
SCOREEa=SCOREE
for (i in 1:dim(SCOREEa)[1]){
  if(SCOREEa[i,1]>0){SCOREEa[i,1]=SCOREEa[i,1]-0.02}
  if(SCOREEa[i,1]<0){SCOREEa[i,1]=SCOREEa[i,1]+0.02}
}
arrows(rep(0,dim(SCOREEa)[1]),rep(0,dim(SCOREEa)[1]),SCOREEa[,1],SCOREE[,3],col="green",length=0.07)
abline(h=0)
abline(v=0)

if (polygoner==TRUE){
  uno=biplotdata$DIM1[1:ngen]
  dos=biplotdata$DIM3[1:ngen] 
  hpts <- chull(x = uno, y = dos)
  d1=cbind(uno[hpts], dos[hpts])
  #d=d1[order(d1[,1],decreasing=F),]
  d=rbind(d1,d1[1,])
  xxx=t(t(rep(0,(nrow(d)-1))))
  yyy=t(t(rep(0,(nrow(d)-1))))
  ppp=matrix(c(0, 1,1 ,0),2,2)
  for (i in 1:(nrow(d)-1)){
  dd=d[i:(i+1),]
  if (dd[1,1]>dd[2,1]){ddd=ppp%*%dd} else{ddd=dd}
  p=(ddd[2,2]-ddd[1,2])/(ddd[2,1]-ddd[1,1])
  if (p<0){ss=1}else {ss=-1}
  r=tan((180-90-abs(atan(p)*180/3.14156))*3.14156/180)*ss 
  aa=(ddd[1,2]+ddd[2,2])/2-p*(ddd[1,1]+ddd[2,1])/2
  xx=aa/(r-p)
  if (abs(r)<1){xxx[i,]=1} else{xxx[i,]=1/abs(r)}
  if (xx<0){xxx[i,]=-xxx[i,]} else{xxx[i,]=xxx[i,]}
  yyy[i,]=xxx[i,]*r
  }
  per=cbind(xxx,yyy)
  lines(d[,1], d[,2], col = "blue",lty=2)
  s1=t(t(rep(0,dim(per)[1])))
  segments(s1,s1,per[,1],per[,2],lty=2)
  }
  dev.off()
  
if (BiplotFormat=="pdf"){pdf(paste("Biplot PC2vsPC3",paste(traits[b],paste(ExpDes,paste(analysis,".pdf")))))}
if (BiplotFormat=="png"){png(paste("Biplot PC2vsPC3",paste(traits[b],paste(ExpDes,paste(analysis,".png")))))}
if (BiplotFormat=="wmf"){win.metafile(paste("Biplot PC2vsPC3",paste(traits[b],paste(ExpDes,paste(analysis,".wmf")))))}

plot(SCOREE[,c(2,3)],type="n",main=paste(analysis,paste(varname,paste("from a",ExpDes))),
     xlab=paste("Factor 2",paste("(",paste(PERC2,"%)"))),
     ylab=paste("Factor 3",paste("(",paste(PERC3,"%)"))),cex=0.7,xlim=c(-1,1),ylim=c(-1,1),
     col.main=c("blue"),col.lab=c("blue"))
text(SCOREG[,c(2,3)],col="blue",cex=0.7,labels=rownames(SCOREG))
text(SCOREE[,c(2,3)],col="red",cex=0.7,labels=rownames(SCOREE))
SCOREEa=SCOREE
for (i in 1:dim(SCOREEa)[1]){
  if(SCOREEa[i,2]>0){SCOREEa[i,2]=SCOREEa[i,2]-0.02}
  if(SCOREEa[i,2]<0){SCOREEa[i,2]=SCOREEa[i,2]+0.02}
}
arrows(rep(0,dim(SCOREEa)[2]),rep(0,dim(SCOREEa)[2]),SCOREEa[,2],SCOREE[,3],col="green",length=0.07)
abline(h=0)
abline(v=0)

if(polygoner==TRUE){
  uno=biplotdata$DIM2[1:ngen]
  dos=biplotdata$DIM3[1:ngen] 
  hpts <- chull(x = uno, y = dos)
  d1=cbind(uno[hpts], dos[hpts])
  #d=d1[order(d1[,1],decreasing=F),]
  d=rbind(d1,d1[1,])
  xxx=t(t(rep(0,(nrow(d)-1))))
  yyy=t(t(rep(0,(nrow(d)-1))))
  ppp=matrix(c(0, 1,1 ,0),2,2)
  for (i in 1:(nrow(d)-1)){
  dd=d[i:(i+1),]
  if (dd[1,1]>dd[2,1]){ddd=ppp%*%dd} else{ddd=dd}
  p=(ddd[2,2]-ddd[1,2])/(ddd[2,1]-ddd[1,1])
  if (p<0){ss=1}else {ss=-1}
  r=tan((180-90-abs(atan(p)*180/3.14156))*3.14156/180)*ss 
  aa=(ddd[1,2]+ddd[2,2])/2-p*(ddd[1,1]+ddd[2,1])/2
  xx=aa/(r-p)
  if (abs(r)<1){xxx[i,]=1} else{xxx[i,]=1/abs(r)}
  if (xx<0){xxx[i,]=-xxx[i,]} else{xxx[i,]=xxx[i,]}
  yyy[i,]=xxx[i,]*r
  }
  per=cbind(xxx,yyy)
  lines(d[,1], d[,2], col = "blue",lty=2)
  s1=t(t(rep(0,dim(per)[1])))
  segments(s1,s1,per[,1],per[,2],lty=2)
  }
  
  dev.off()
}
 
 
if (BiplotFormat=="pdf"){pdf(paste("PC1vsTrait",paste(traits[b],paste(ExpDes,paste(analysis,".pdf")))))}
if (BiplotFormat=="png"){png(paste("PC1vsTrait",paste(traits[b],paste(ExpDes,paste(analysis,".png")))))}
if (BiplotFormat=="wmf"){win.metafile(paste("PC1vsTrait",paste(traits[b],paste(ExpDes,paste(analysis,".wmf")))))}

  minx=round(min(yldgen,as.numeric(new3[,2])))-0.5
  maxx=round(max(yldgen,as.numeric(new3[,2])))+0.5
  plot(SCOREE[,c(1,2)],type="n",main=paste(analysis,paste("PCA1 Score vs",paste(varname,paste("from a",ExpDes)))),
       xlab=paste(varname),var.axes=F,expand=2,
       ylab=paste("Factor 1",paste("(",paste(PERC1,"%)"))),cex=0.8,xlim=c(minx,maxx),ylim=c(-1,1),
       col.main=c("blue"),col.lab=c("blue"))
  
  text(cbind(yldgen,SCOREG[,1]),col="blue",cex=0.7,labels=rownames(SCOREG))
  text(cbind(as.numeric(new3[,2]),SCOREE[,1]),col="red",cex=0.7,labels=rownames(SCOREE))
  myld=mean(yldgen)
  numa=as.numeric(new3[,2])
  for (j in 1:dim(SCOREE)[1]){
    if(numa[j]>0){numa[j]=numa[j]-0.07}
    if(numa[j]<0){numa[j]=numa[j]+0.07}
  }
  arrows(rep(myld,dim(SCOREE)[1]),rep(0,dim(SCOREE)[1]),numa,SCOREE[,1],col="green",length=0.07)
  abline(h=0)
  abline(v=myld)
dev.off()

##3D Graph
if (nenv>2){
if (plot3D==TRUE){
biplotdataENV=biplotdata[biplotdata$TYPE=="ENV",]
biplotdataGEN=biplotdata[biplotdata$TYPE=="GEN",]

library(plotly)
cero=cbind(biplotdataENV[1,1:2],t(rep(0,4)))
names(cero)=names(biplotdataENV)
nada=cbind(biplotdataENV[1,1:2],t(c("NA","NA","NA",0)))
names(nada)=names(biplotdataENV)

  biplotdataENV1=rbind(cero,biplotdataENV[1,],nada)
for (i in 2:dim(biplotdataENV)[1]){
  biplotdataENV1=rbind(biplotdataENV1,rbind(cero,biplotdataENV[i,],nada))
}

biplotdataENV1$YLD=as.numeric(biplotdataENV1$YLD)
biplotdataENV1$DIM1=as.numeric(biplotdataENV1$DIM1)
biplotdataENV1$DIM2=as.numeric(biplotdataENV1$DIM2)
biplotdataENV1$DIM3=as.numeric(biplotdataENV1$DIM3)

mds3= plot_ly(biplotdataGEN,x= ~DIM1,y= ~DIM2,z= ~DIM3,type='scatter3d',mode='markers',marker=list(color='blue'),text = paste('GEN: ', as.character(biplotdataGEN$NAME)))%>%
      layout(scene=list(xaxis=list(title=paste('Factor 1',paste('(',paste(PERC1,'%)')))),
                    yaxis=list(title=paste('Factor 2',paste('(',paste(PERC2,'%)')))),
                    zaxis=list(title=paste('Factor 3',paste('(',paste(PERC3,'%)'))))),
             showlegend = FALSE)%>%
      add_trace(data=biplotdataENV1, x=~biplotdataENV1$DIM1, y=~biplotdataENV1$DIM2, z=~biplotdataENV1$DIM3, showlegend = FALSE,
                type = 'scatter3d', mode = 'lines+markers',connectgaps=FALSE,
                line=list(color="red"),marker=list(size=5,color="red"),text = paste("ENV: ", as.character(biplotdataENV1$NAME)))
htmlwidgets::saveWidget(as.widget(mds3), selfcontained = FALSE, "Biplot3D.html")






#ver1=matrix(0,dim(SCOREE)[1],3)
#ver2=rbind(ver1[1,],SCOREE[1,])
#for (i in 2:dim(SCOREE)[1]){
#  ver2=rbind(ver2,ver1[i,],SCOREE[i,])
#}

#open3d(windowRect = c(83, 105, 1000, 1000) ) 
#plot3d(SCOREG[,1],SCOREG[,2],SCOREG[,3],
#       xlim=c(-1,1),ylim=c(-1,1),zlim=c(-1,1),type="n",
#       xlab=paste("Factor 1",paste("(",paste(PERC1,"%)"))),
#       ylab=paste("Factor 2",paste("(",paste(PERC2,"%)"))),
#       zlab=paste("Factor 3",paste("(",paste(PERC3,"%)"))))
#texts3d(SCOREG[,1],SCOREG[,2],SCOREG[,3],rownames(SCOREG), col="blue")
#texts3d(SCOREE[,1],SCOREE[,2],SCOREE[,3],rownames(SCOREE),col="red")
#segments3d(ver2,col="green")
#abclines3d(0,0,0,a=diag(3))

#mywait()



}
}


}

}

