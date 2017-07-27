REGFACT<-function(datos=datos,file_nameCOV,ExpDes=ExpDes,traits=traits,selected=selected,typecov=typecov,cpv=cpv,tmp=tmp){
rm(list=ls())

library(car)
suppressWarnings(library(Hmisc))
#Modify Env = ENV,Rep=REP,Block= BLOCK and Loc = ENV,Entry = GEN
#Covariate = file_nameCOV instead of read.csv(file_nameCOV)
orgdir=getwd()

 for (b in 1:length(traits)){  
  newfold=paste("OutputFactReg&",paste(tmp,paste(ExpDes,paste("&",traits[b],sep=""),sep=""),sep=""),sep="")
  sal=paste(orgdir,paste("/",newfold,sep=""),sep="")
  dir.create(sal)
  setwd(sal)
  out=paste("ResultFactorialRegression",paste(ExpDes,paste("Cov",paste(typecov,paste(traits[b],".csv",sep=""),sep="")
                                          ,sep=""),sep=""),sep="") 

if (ExpDes=="LSMeans"){
raw=datos
  if( typecov=="markers" || typecov=="gen") {raw=raw[order(raw$ENV,raw$GEN),]}
  if( typecov=="env") {raw=raw[order(raw$GEN,raw$ENV),]}
  index <- which(as.character(raw$ENV)%in%selected)
  if(length(index)>0)	raw <- raw[index,]
  
  Covariate=file_nameCOV
  Covariate=Covariate[order(Covariate[,1]),]
  indexCOV <- which(as.character(Covariate[,1])%in%selected)
  if(length(indexCOV)>0)	Covariate <- Covariate[indexCOV,]
  Covp=Covariate[,-1]
  
  if( typecov=="markers" || typecov=="gen"){
  for (i in 1:(length(selected)-1)){
       Covp=rbind(Covp,Covariate[,-1])
  }
  }
  
  if( typecov=="env"){
  for (i in 1:(nlevels(as.factor(as.character(raw$GEN)))-1)){
       Covp=rbind(Covp,Covariate[,-1])
  }
  }
    raw=as.data.frame(cbind(ENV=raw$ENV,GEN=raw$GEN,YLD=as.numeric(as.character(raw[,traits[b]]))))
    raw$GEN=as.factor(raw$GEN)
    raw$ENV=as.factor(raw$ENV)
    raw$YLD=as.numeric(as.character(raw$YLD))
    varname=traits[b]
    colnames(raw)[3]=c("YLD")
  }
  
  if (ExpDes=="RCB"){
  raw=datos
  if( typecov=="markers" || typecov=="gen") {raw=raw[order(raw$ENV,raw$REP,raw$GEN),]}
  if( typecov=="env") {raw=raw[order(raw$GEN,raw$REP,raw$ENV),]}
  index <- which(as.character(raw$ENV)%in%selected)
  if(length(index)>0)	raw <- raw[index,]
  
  Covariate=file_nameCOV
  Covariate=Covariate[order(Covariate[,1]),]
  indexCOV <- which(as.character(Covariate[,1])%in%selected)
  if(length(indexCOV)>0)	Covariate <- Covariate[indexCOV,]
  Covp=Covariate[,-1]
  
  if( typecov=="markers" || typecov=="gen"){
  for (i in 1:(length(selected)*nlevels(as.factor(as.character(raw$REP)))-1)){
       Covp=rbind(Covp,Covariate[,-1])
  }
  }
  
  if( typecov=="env"){
  for (i in 1:(nlevels(as.factor(as.character(raw$GEN)))*nlevels(as.factor(as.character(raw$REP)))-1)){
       Covp=rbind(Covp,Covariate[,-1])
  }
  }
    raw=as.data.frame(cbind(ENV=raw$ENV,GEN=raw$GEN,REP=raw$REP,YLD=as.numeric(as.character(raw[,traits[b]]))))
    raw$GEN=as.factor(raw$GEN)
    raw$ENV=as.factor(raw$ENV)
    raw$REP=as.factor(raw$REP)
    raw$YLD=as.numeric(as.character(raw$YLD))
    varname=traits[b]
    colnames(raw)[4]=c("YLD")
  }
  
  if (ExpDes=="Lattice"){
  raw=datos
  if( typecov=="markers" || typecov=="gen") {raw=raw[order(raw$ENV,raw$REP,raw$GEN),]}
  if( typecov=="env") {raw=raw[order(raw$GEN,raw$REP,raw$ENV),]}
  index <- which(as.character(raw$ENV)%in%selected)
  if(length(index)>0)	raw <- raw[index,]
  
  Covariate=file_nameCOV
  Covariate=Covariate[order(Covariate[,1]),]
  indexCOV <- which(as.character(Covariate[,1])%in%selected)
  if(length(indexCOV)>0)	Covariate <- Covariate[indexCOV,]
  Covp=Covariate[,-1]
  
  if( typecov=="markers" || typecov=="gen"){
  for (i in 1:(length(selected)*nlevels(as.factor(as.character(raw$REP)))-1)){
       Covp=rbind(Covp,Covariate[,-1])
  }
  }
  
  if( typecov=="env"){
  for (i in 1:(nlevels(as.factor(as.character(raw$GEN)))*nlevels(as.factor(as.character(raw$REP)))-1)){
       Covp=rbind(Covp,Covariate[,-1])
  }
  }
    raw=as.data.frame(cbind(ENV=raw$ENV,GEN=raw$GEN,REP=raw$REP,BLOCK=raw$BLOCK,YLD=as.numeric(as.character(raw[,traits[b]]))))
    raw$GEN=as.factor(raw$GEN)
    raw$ENV=as.factor(raw$ENV)
    raw$REP=as.factor(raw$REP)
    raw$BLOCK=as.factor(raw$BLOCK)
    raw$YLD=as.numeric(as.character(raw$YLD))
    varname=traits[b]
    colnames(raw)[5]=c("YLD")
  }										  
  
if (ExpDes=="RCB"){
  if(typecov=="markers"){ncov="+ENV*"}
  if(typecov=="gen"){ncov="+ENV*"}
  if(typecov=="env"){ncov="+GEN*"}
  
  raw=cbind(raw,Covp)
  
  for (i in 5:dim(raw)[2]){
    raw[,i]=as.numeric(as.character(raw[,i]))
  }
  
  uno=c("YLD ~ENV+REP%in%ENV+GEN")
  
  if(dim(raw)[2]>53){
    aicm=list()
    sigval=list()
    namesvar=list()
    numchoice=list()
    j=1
    for (i in 5:dim(raw)[2]){
      dos=as.formula(paste(uno,paste("+ENV*",names(raw)[i])))
      cmodel=lm(dos,data=raw,na.action=na.omit)
      aicm[[j]]=AIC(cmodel)
      
      if(aicm[[j]]!="-Inf"){
        manova=Anova(cmodel)
        sigval[[j]]=manova[(dim(manova)[1]-1),4]
        namesvar[[j]]=paste("+ENV*",names(raw)[i])
        numchoice[[j]]=i}
      
      if(aicm[[j]]=="-Inf"){
        stop("AIC=-Inf")}
      
      j=j+1}
    
    sigval=unlist(sigval)
    aicm=unlist(aicm)
    namesvar=unlist(namesvar)
    
    useful=which(sigval<=cpv)+4
    datos=raw[,c(1,2,3,4,useful)]
  }
  
  if(dim(raw)[2]<53){
    datos=raw
  }
  
  steps=list()
  choices=dim(datos)[2]+1
  elmod=0
  
  for (k in 1:(dim(datos)[2]-4)){
    aicm=list()
    sigval=list()
    others=list()
    namesvar=list()
    numchoice=list()
    j=1
    for (i in 5:dim(datos)[2]){
      if (i%in%(choices)==FALSE){
        dos=as.formula(paste(uno,paste(ncov,names(datos)[i])))
        cmodel=lm(dos,data=datos,na.action=na.omit)
        aicm[[j]]=AIC(cmodel)
        
        if(aicm[[j]]!="-Inf"){
          manova=Anova(cmodel)
          sigval[[j]]=ifelse(is.na(manova[(dim(manova)[1]-1),4])==TRUE,10000,manova[(dim(manova)[1]-1),4])
          others[[j]]=c(manova[(dim(manova)[1]-1),1],manova[(dim(manova)[1]-1),2],manova[(dim(manova)[1]-1),3])
          namesvar[[j]]=paste(ncov,names(datos)[i])
          numchoice[[j]]=i}
        
        if(aicm[[j]]=="-Inf"){
          general=lm(YLD~ENV+GEN+REP%in%ENV+GEN*ENV,data=datos,na.action=na.omit)
          angeneral=round(Anova(general),5)
          rowgen=c("*",rownames(angeneral))
          angeneral=rbind(colnames(angeneral),angeneral)
          angeneral=cbind(t(t(rowgen)),angeneral)
          aicgeneral=c("AIC general model",AIC(general))
          
          bestmodel=lm(as.formula(uno),data=datos)
          anbest=round(as.data.frame(Anova(bestmodel)),5)
          rowbest=c("*",rownames(anbest))
          anbest=rbind(colnames(anbest),anbest)
          anbest=cbind(t(t(rowbest)),anbest)
          aicbest=c("AIC selected model",AIC(bestmodel))
          anbest=anbest[-which(is.na(anbest[,2])),]
		  
          steps1=matrix(unlist(steps),length(steps),7,byrow=T)
          steps1[,1]=unique(unlist(strsplit(steps1[,1],"[+]")))[-1]
		  steps1=rbind(c("Effect name","Sum Sq","Df","Fvalue","AIC","Pr>F","TorF"),steps1)
          steps1=as.data.frame(steps1)
		  pertge=c("%GxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]-1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]),"*")
          pertgeA=c("%AcumGxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),c("*",cumsum(as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]-1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]))[-1]),"*")
          anbest=cbind(anbest,pertge,pertgeA)
          
          
          cat("RESULTS FOR FACTORIAL REGRESSION","\n",file=out)
          cat("\n","\n", "GENERAL MODEL","\n", file=out, append = T)
          cat("\n", traits[b],"~ENV+GEN+REP%in%ENV+GEN*ENV","\n", file=out, append = T)
          cat("\n", aicgeneral,"\n", file=out, append = T)
          cat("\n",file=out, append = T)
          write.table(angeneral, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
          #print.char.matrix(round(angeneral, 5), file = out, col.names = T, append = T)
          cat("\n","\n","\n", "SELECTED MODEL","\n", file=out, append = T)
          cat("\n", uno,"\n", file=out, append = T)
          cat("\n", aicbest,"\n", file=out, append = T)
          cat("\n",file=out, append = T)
          write.table(anbest, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
          #print.char.matrix(round(anbest, 5), file = out, col.names = T, append = T)
          cat("\n","\n","\n", "STEPS FOR FACTORIAL REGRESSION","\n", file=out, append = T)
          write.table(steps1, file = out, col.names = F, append = T,quote=F, sep=",",row.names=F)
          #print.char.matrix(steps1, file = out, col.names = T, append = T)
          #file.show(out)
          stop("AIC=-Inf")}
        
        j=j+1}
    }
    
    sigval=unlist(sigval)
    aicm=unlist(aicm)
    namesvar=unlist(namesvar)
    numchoice=unlist(numchoice)
    bestvar1=which(sigval==min(sigval,na.rm=T))[1]
    
    
    
    if(sigval[bestvar1]<=cpv){check1=cbind(namesvar[bestvar1],t(others[[bestvar1]]),aicm[bestvar1],sigval[bestvar1],c("effect entered"));steps[[k]]=check1
                              uno=paste(uno,namesvar[bestvar1]);choices=cbind(choices,numchoice[bestvar1]);elmod=elmod+1
                              tres=as.formula(uno)
                              cmodelc=lm(tres,data=datos,na.action=na.omit)
                              manovac=Anova(cmodelc)
                              sign=manovac[(4+elmod):(dim(manovac)[1]-1),4]
                              namesign=rownames(manovac)[(4+elmod):(dim(manovac)[1]-1)]
                              
                              if (length(which(sign>cpv))!=0){
                                namesign=namesign[-(which(sign>cpv))]
                                mnew=c("YLD ~ENV+REP%in%ENV+GEN")
                                for (w in 1:length(namesign)){mnew=paste(mnew,paste("+",namesign[w]))}
                                uno=mnew                            
                              }
                              
    }
    
    
    
    if(sigval[bestvar1]>cpv){uno=uno;choices=cbind(choices,numchoice[bestvar1])}
    
  }
  
  general=lm(YLD~ENV+GEN+REP%in%ENV+GEN*ENV,data=datos,na.action=na.omit)
  angeneral=round(Anova(general),5)
  rowgen=c("*",rownames(angeneral))
  angeneral=rbind(colnames(angeneral),angeneral)
  angeneral=cbind(t(t(rowgen)),angeneral)
  aicgeneral=c("AIC general model",AIC(general))
  
  bestmodel=lm(as.formula(uno),data=datos)
  anbest=round(as.data.frame(Anova(bestmodel)),5)
  rowbest=c("*",rownames(anbest))
  anbest=rbind(colnames(anbest),anbest)
  anbest=cbind(t(t(rowbest)),anbest)
  aicbest=c("AIC selected model",AIC(bestmodel))
  anbest=anbest[-which(is.na(anbest[,2])),]
  
  steps1=matrix(unlist(steps),length(steps),7,byrow=T)
  steps1[,1]=unique(unlist(strsplit(steps1[,1],"[+]")))[-1]
  steps1=rbind(c("Effect name","Sum Sq","Df","Fvalue","AIC","Pr>F","TorF"),steps1)
  steps1=as.data.frame(steps1)
  
  pertge=c("%GxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]-1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]),"*")
  pertgeA=c("%AcumGxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),c("*",cumsum(as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]-1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]))[-1]),"*")
  anbest=cbind(anbest,pertge,pertgeA)
  
  cat("RESULTS FOR FACTORIAL REGRESSION","\n",file=out)
  cat("\n","\n", "GENERAL MODEL","\n", file=out, append = T)
  cat("\n", traits[b],"~ENV+GEN+REP%in%ENV+GEN*ENV","\n", file=out, append = T)
  cat("\n", aicgeneral,"\n", file=out, append = T)
  cat("\n",file=out, append = T)
  write.table(angeneral, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
  #print.char.matrix(round(angeneral, 5), file = out, col.names = T, append = T)
  cat("\n","\n","\n", "SELECTED MODEL","\n", file=out, append = T)
  cat("\n", uno,"\n", file=out, append = T)
  cat("\n", aicbest,"\n", file=out, append = T)
  cat("\n",file=out, append = T)
  write.table(anbest, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
  #print.char.matrix(round(anbest, 5), file = out, col.names = T, append = T)
  cat("\n","\n","\n", "STEPS FOR FACTORIAL REGRESSION","\n", file=out, append = T)
  write.table(steps1, file = out, col.names = F, append = T,quote=F, sep=",",row.names=F)
  #print.char.matrix(steps1, file = out, col.names = T, append = T)
  #file.show(out)
  
}

if (ExpDes=="Lattice"){
  
  if(typecov=="markers"){ncov="+ENV*"}
  if(typecov=="gen"){ncov="+ENV*"}
  if(typecov=="env"){ncov="+GEN*"}
  
  raw=cbind(raw,Covp)
  
  for (i in 6:dim(raw)[2]){
    raw[,i]=as.numeric(as.character(raw[,i]))
  }
  
  uno=c("YLD ~ENV+GEN+REP%in%ENV+BLOCK%in%(REP%in%ENV)")
  
  if(dim(raw)[2]>53){
    aicm=list()
    sigval=list()
    namesvar=list()
    numchoice=list()
    j=1
    for (i in 6:dim(raw)[2]){
      dos=as.formula(paste(uno,paste("+ENV*",names(raw)[i])))
      cmodel=lm(dos,data=raw,na.action=na.omit)
      aicm[[j]]=AIC(cmodel)
      
      if(aicm[[j]]!="-Inf"){
        manova=Anova(cmodel)
        sigval[[j]]=manova[(dim(manova)[1]-2),4]
        namesvar[[j]]=paste("+ENV*",names(raw)[i])
        numchoice[[j]]=i}
      
      if(aicm[[j]]=="-Inf"){
        stop("AIC=-Inf")}
      
      j=j+1}
    
    sigval=unlist(sigval)
    aicm=unlist(aicm)
    namesvar=unlist(namesvar)
    
    useful=which(sigval<=cpv)+5
    datos=raw[,c(1,2,3,4,5,useful)]
  }
  
  if(dim(raw)[2]<53){
    datos=raw
  }
  
  steps=list()
  choices=dim(datos)[2]+1
  elmod=0
  
  for (k in 1:(dim(datos)[2]-5)){
    aicm=list()
    sigval=list()
    others=list()
    namesvar=list()
    numchoice=list()
    j=1
    for (i in 6:dim(datos)[2]){
      if (i%in%(choices)==FALSE){
        dos=as.formula(paste(uno,paste(ncov,names(datos)[i])))
        cmodel=lm(dos,data=datos,na.action=na.omit)
        aicm[[j]]=AIC(cmodel)
        
        if(aicm[[j]]!="-Inf"){
          manova=Anova(cmodel)
          sigval[[j]]=ifelse(is.na(manova[(dim(manova)[1]-2),4])==TRUE,10000,manova[(dim(manova)[1]-2),4])
          others[[j]]=c(manova[(dim(manova)[1]-2),1],manova[(dim(manova)[1]-2),2],manova[(dim(manova)[1]-2),3])
          namesvar[[j]]=paste(ncov,names(datos)[i])
          numchoice[[j]]=i}
        
        if(aicm[[j]]=="-Inf"){
          general=lm(YLD~ENV+GEN+REP%in%ENV+BLOCK%in%(REP%in%ENV)+GEN:ENV,data=datos)
          angeneral=round(Anova(general),5)
          rowgen=c("*",rownames(angeneral))
          angeneral=rbind(colnames(angeneral),angeneral)
          angeneral=cbind(t(t(rowgen)),angeneral)
          aicgeneral=c("AIC general model",AIC(general))
          
          bestmodel=lm(as.formula(uno),data=datos)
          anbest=round(as.data.frame(Anova(bestmodel)),5)
          rowbest=c("*",rownames(anbest))
          anbest=rbind(colnames(anbest),anbest)
          anbest=cbind(t(t(rowbest)),anbest)
          aicbest=c("AIC selected model",AIC(bestmodel))
          anbest=anbest[-which(is.na(anbest[,2])),]
		  
          steps1=matrix(unlist(steps),length(steps),7,byrow=T)
          steps1[,1]=unique(unlist(strsplit(steps1[,1],"[+]")))[-1]
          steps1=rbind(c("Effect name","Sum Sq","Df","Fvalue","AIC","Pr>F","TorF"),steps1)
          steps1=as.data.frame(steps1)
		  
		  pertge=c("%GxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-2)),as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1])):(dim(anbest)[1]-2),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-2),2]),"*","*")
          pertgeA=c("%AcumGxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-2)),c("*",cumsum(as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1])):(dim(anbest)[1]-2),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-2),2]))[-1]),"*","*")
          anbest=cbind(anbest,pertge,pertgeA)
          
          cat("RESULTS FOR FACTORIAL REGRESSION","\n",file=out)
          cat("\n","\n", "GENERAL MODEL","\n", file=out, append = T)
          cat("\n", traits[b],"~ENV+GEN+REP%in%ENV+BLOCK%in%(REP%in%ENV)+GEN:ENV","\n", file=out, append = T)
          cat("\n", aicgeneral,"\n", file=out, append = T)
          cat("\n",file=out, append = T)
          write.table(angeneral, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
          #print.char.matrix(round(angeneral, 5), file = out, col.names = T, append = T)
          cat("\n","\n","\n", "SELECTED MODEL","\n", file=out, append = T)
          cat("\n", uno,"\n", file=out, append = T)
          cat("\n", aicbest,"\n", file=out, append = T)
          cat("\n",file=out, append = T)
          write.table(anbest, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
          #print.char.matrix(round(anbest, 5), file = out, col.names = T, append = T)
          cat("\n","\n","\n", "STEPS FOR FACTORIAL REGRESSION","\n", file=out, append = T)
          write.table(steps1, file = out, col.names = F, append = T,quote=F, sep=",",row.names=F)
          #print.char.matrix(steps1, file = out, col.names = T, append = T)
          #file.show(out)
          stop("AIC=-Inf")}
        
        j=j+1}
    }
    
    sigval=unlist(sigval)
    aicm=unlist(aicm)
    namesvar=unlist(namesvar)
    numchoice=unlist(numchoice)
    bestvar1=which(sigval==min(sigval,na.rm=T))[1]
    
    if(sigval[bestvar1]<=cpv){check1=cbind(namesvar[bestvar1],t(others[[bestvar1]]),aicm[bestvar1],sigval[bestvar1],c("effect entered"));steps[[k]]=check1
                              uno=paste(uno,namesvar[bestvar1]);choices=cbind(choices,numchoice[bestvar1]);elmod=elmod+1
                              tres=as.formula(uno)
                              cmodelc=lm(tres,data=datos,na.action=na.omit)
                              manovac=Anova(cmodelc)
                              sign=manovac[(4+elmod):(dim(manovac)[1]-2),4]
                              namesign=rownames(manovac)[(4+elmod):(dim(manovac)[1]-2)]
                              
                              if (length(which(sign>cpv))!=0){
                                namesign=namesign[-(which(sign>cpv))]
                                mnew=c("YLD ~ENV+GEN+REP%in%ENV+BLOCK%in%(REP%in%ENV)")
                                for (w in 1:length(namesign)){mnew=paste(mnew,paste("+",namesign[w]))}
                                uno=mnew                            
                              }
                              
    }
    
    
    #check1=cbind(namesvar[bestvar1],aicm[bestvar1],sigval[bestvar1],c("effect NO entered"));steps[[k]]=check1
    if(sigval[bestvar1]>cpv){uno=uno;choices=cbind(choices,numchoice[bestvar1])}
    
  }
  
  
  general=lm(YLD~ENV+GEN+REP%in%ENV+BLOCK%in%(REP%in%ENV)+GEN:ENV,data=datos)
  angeneral=round(Anova(general),5)
  rowgen=c("*",rownames(angeneral))
  angeneral=rbind(colnames(angeneral),angeneral)
  angeneral=cbind(t(t(rowgen)),angeneral)
  aicgeneral=c("AIC general model",AIC(general))
  
  bestmodel=lm(as.formula(uno),data=datos)
  anbest=round(as.data.frame(Anova(bestmodel)),5)
  rowbest=c("*",rownames(anbest))
  anbest=rbind(colnames(anbest),anbest)
  anbest=cbind(t(t(rowbest)),anbest)
  aicbest=c("AIC selected model",AIC(bestmodel))
  anbest=anbest[-which(is.na(anbest[,2])),]
  
  steps1=matrix(unlist(steps),length(steps),7,byrow=T)
  steps1[,1]=unique(unlist(strsplit(steps1[,1],"[+]")))[-1]
  steps1=rbind(c("Effect name","Sum Sq","Df","Fvalue","AIC","Pr>F","TorF"),steps1)
  steps1=as.data.frame(steps1)
  pertge=c("%GxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-2)),as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1])):(dim(anbest)[1]-2),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-2),2]),"*","*")
  pertgeA=c("%AcumGxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-2)),c("*",cumsum(as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1])):(dim(anbest)[1]-2),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-2),2]))[-1]),"*","*")
  anbest=cbind(anbest,pertge,pertgeA)
  
  cat("RESULTS FOR FACTORIAL REGRESSION","\n",file=out)
  cat("\n","\n", "GENERAL MODEL","\n", file=out, append = T)
  cat("\n", traits[b],"~ENV+GEN+REP%in%ENV+BLOCK%in%(REP%in%ENV)+GEN:ENV","\n", file=out, append = T)
  cat("\n", aicgeneral,"\n", file=out, append = T)
  cat("\n",file=out, append = T)
  write.table(angeneral, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
  #print.char.matrix(round(angeneral, 5), file = out, col.names = T, append = T)
  cat("\n","\n","\n", "SELECTED MODEL","\n", file=out, append = T)
  cat("\n", uno,"\n", file=out, append = T)
  cat("\n", aicbest,"\n", file=out, append = T)
  cat("\n",file=out, append = T)
  write.table(anbest, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
  #print.char.matrix(round(anbest, 5), file = out, col.names = T, append = T)
  cat("\n","\n","\n", "STEPS FOR FACTORIAL REGRESSION","\n", file=out, append = T)
  write.table(steps1, file = out, col.names = F, append = T,quote=F, sep=",",row.names=F)
  #print.char.matrix(steps1, file = out, col.names = T, append = T)
  #file.show(out)
  
}

if (ExpDes=="LSMeans"){
  
  if(typecov=="markers"){ncov="+ENV*"}
  if(typecov=="gen"){ncov="+ENV*"}
  if(typecov=="env"){ncov="+GEN*"}
  
  raw=cbind(raw,Covp)
  
  uno=c("YLD ~ENV+GEN")
  
  if(dim(raw)[2]>53){
    aicm=list()
    sigval=list()
    namesvar=list()
    numchoice=list()
    j=1
    for (i in 4:dim(raw)[2]){
      dos=as.formula(paste(uno,paste("+ENV*",names(raw)[i])))
      cmodel=lm(dos,data=raw,na.action=na.omit)
      aicm[[j]]=AIC(cmodel)
    
    if(aicm[[j]]!="-Inf"){
      manova=Anova(cmodel)
      sigval[[j]]=manova[(dim(manova)[1]-1),4]
      namesvar[[j]]=paste("+ENV*",names(raw)[i])
      numchoice[[j]]=i}
    
    if(aicm[[j]]=="-Inf"){
      stop("AIC=-Inf")}
    
    j=j+1}
  
    sigval=unlist(sigval)
    aicm=unlist(aicm)
    namesvar=unlist(namesvar)
  
    useful=which(sigval<=cpv)+3
    datos=raw[,c(1,2,3,useful)]
  }
  
  if(dim(raw)[2]<53){
  datos=raw
  }
  
  
  steps=list()
  choices=dim(datos)[2]+1
  elmod=0
  
  for (k in 1:(dim(datos)[2]-3)){
    aicm=list()
    sigval=list()
    others=list()
    namesvar=list()
    numchoice=list()
    j=1
    for (i in 4:dim(datos)[2]){
      if (i%in%(choices)==FALSE){
        dos=as.formula(paste(uno,paste(ncov,names(datos)[i])))
        cmodel=lm(dos,data=datos,na.action=na.omit)
        aicm[[j]]=AIC(cmodel)
        
        if(aicm[[j]]!="-Inf"){
          manova=Anova(cmodel)
          sigval[[j]]=ifelse(is.na(manova[(dim(manova)[1]-1),4])==TRUE,10000,manova[(dim(manova)[1]-1),4])
          others[[j]]=c(manova[(dim(manova)[1]-1),1],manova[(dim(manova)[1]-1),2],manova[(dim(manova)[1]-1),3])
          namesvar[[j]]=paste(ncov,names(datos)[i])
          numchoice[[j]]=i}
        
        if(aicm[[j]]=="-Inf"){
          general=lm(YLD~ENV+GEN+GEN*ENV,data=datos)
          angeneral=round(Anova(general),5)
          rowgen=c("*",rownames(angeneral))
          angeneral=rbind(colnames(angeneral),angeneral)
          angeneral=cbind(t(t(rowgen)),angeneral)
          aicgeneral=c("AIC general model",AIC(general))
          
          bestmodel=lm(as.formula(uno),data=datos)
          anbest=round(as.data.frame(Anova(bestmodel)),5)
          rowbest=c("*",rownames(anbest))
          anbest=rbind(colnames(anbest),anbest)
          anbest=cbind(t(t(rowbest)),anbest)
          aicbest=c("AIC selected model",AIC(bestmodel))
          anbest=anbest[-which(is.na(anbest[,2])),]
		  
          steps1=matrix(unlist(steps),length(steps),7,byrow=T)
          steps1[,1]=unique(unlist(strsplit(steps1[,1],"[+]")))[-1]
          steps1=rbind(c("Effect name","Sum Sq","Df","Fvalue","AIC","Pr>F","TorF"),steps1)
          steps1=as.data.frame(steps1)
		  pertge=c("%GxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]+1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]),"*")
          pertgeA=c("%AcumGxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),c("*",cumsum(as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]+1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]))[-1]),"*")
          anbest=cbind(anbest,pertge,pertgeA)
          
          cat("RESULTS FOR FACTORIAL REGRESSION","\n",file=out)
          cat("\n","\n", "GENERAL MODEL","\n", file=out, append = T)
          cat("\n", traits[b],"~ENV+GEN+GEN*ENV","\n", file=out, append = T)
          cat("\n", aicgeneral,"\n", file=out, append = T)
          cat("\n",file=out, append = T)
          write.table(angeneral, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
          #print.char.matrix(round(angeneral, 5), file = out, col.names = T, append = T)
          cat("\n","\n","\n", "SELECTED MODEL","\n", file=out, append = T)
          cat("\n", uno,"\n", file=out, append = T)
          cat("\n", aicbest,"\n", file=out, append = T)
          cat("\n",file=out, append = T)
          write.table(anbest, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
          #print.char.matrix(round(anbest, 5), file = out, col.names = T, append = T)
          cat("\n","\n","\n", "STEPS FOR FACTORIAL REGRESSION","\n", file=out, append = T)
          write.table(steps1, file = out, col.names = F, append = T,quote=F, sep=",",row.names=F)
          #print.char.matrix(steps1, file = out, col.names = T, append = T)
          #file.show(out)
          stop("AIC=-Inf")}
        
        j=j+1}
    }
    
    sigval=unlist(sigval)
    aicm=unlist(aicm)
    namesvar=unlist(namesvar)
    numchoice=unlist(numchoice)
    bestvar1=which(sigval==min(sigval,na.rm=T))[1]
            
    if(sigval[bestvar1]<=cpv){check1=cbind(namesvar[bestvar1],t(others[[bestvar1]]),aicm[bestvar1],sigval[bestvar1],c("effect entered"));steps[[k]]=check1
                              uno=paste(uno,namesvar[bestvar1]);choices=cbind(choices,numchoice[bestvar1]);elmod=elmod+1
                              tres=as.formula(uno)
                              cmodelc=lm(tres,data=datos,na.action=na.omit)
                              manovac=Anova(cmodelc)
                              sign=manovac[(3+elmod):(dim(manovac)[1]-1),4]
                              namesign=rownames(manovac)[(3+elmod):(dim(manovac)[1]-1)]
                              
                              if (length(which(sign>cpv))!=0){
                                namesign=namesign[-(which(sign>cpv))]
                                mnew=c("YLD ~ENV+GEN")
                                for (w in 1:length(namesign)){mnew=paste(mnew,paste("+",namesign[w]))}
                                uno=mnew                            
                              }
                              
    }
    
    
    
    if(sigval[bestvar1]>cpv){uno=uno;choices=cbind(choices,numchoice[bestvar1])}
    
  }
  
  general=lm(YLD~ENV+GEN+GEN*ENV,data=datos)
  angeneral=round(Anova(general),5)
  rowgen=c("*",rownames(angeneral))
  angeneral=rbind(colnames(angeneral),angeneral)
  angeneral=cbind(t(t(rowgen)),angeneral)
  aicgeneral=c("AIC general model",AIC(general))
  
  bestmodel=lm(as.formula(uno),data=datos)
  anbest=round(as.data.frame(Anova(bestmodel)),5)
  rowbest=c("*",rownames(anbest))
  anbest=rbind(colnames(anbest),anbest)
  anbest=cbind(t(t(rowbest)),anbest)
  aicbest=c("AIC selected model",AIC(bestmodel))
  anbest=anbest[-which(is.na(anbest[,2])),]
  
  steps1=matrix(unlist(steps),length(steps),7,byrow=T)
  steps1[,1]=unique(unlist(strsplit(steps1[,1],"[+]")))[-1]
  steps1=rbind(c("Effect name","Sum Sq","Df","Fvalue","AIC","Pr>F","TorF"),steps1)
  steps1=as.data.frame(steps1)
  pertge=c("%GxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]+1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]),"*")
  pertgeA=c("%AcumGxE",rep("*",(dim(anbest)[1]-dim(steps1)[1]-1)),c("*",cumsum(as.numeric(anbest[(dim(anbest)[1]-(dim(steps1)[1]+1)):(dim(anbest)[1]-1),2])*100/as.numeric(angeneral[(dim(angeneral)[1]-1),2]))[-1]),"*")
  anbest=cbind(anbest,pertge,pertgeA)
  
  cat("RESULTS FOR FACTORIAL REGRESSION","\n",file=out)
  cat("\n","\n", "GENERAL MODEL","\n", file=out, append = T)
  cat("\n", traits[b],"~ENV+GEN+GEN*ENV","\n", file=out, append = T)
  cat("\n", aicgeneral,"\n", file=out, append = T)
  cat("\n",file=out, append = T)
  write.table(angeneral, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
  #print.char.matrix(round(angeneral, 5), file = out, col.names = T, append = T)
  cat("\n","\n","\n", "SELECTED MODEL","\n", file=out, append = T)
  cat("\n", uno,"\n", file=out, append = T)
  cat("\n", aicbest,"\n", file=out, append = T)
  cat("\n",file=out, append = T)
  write.table(anbest, file = out, append = T,quote=F, sep=",",col.names=F,row.names=F)
  #print.char.matrix(round(anbest, 5), file = out, col.names = T, append = T)
  cat("\n","\n","\n", "STEPS FOR FACTORIAL REGRESSION","\n", file=out, append = T)
  write.table(steps1, file = out, col.names = F, append = T,quote=F, sep=",",row.names=F)
  #print.char.matrix(steps1, file = out, col.names = T, append = T)
  #file.show(out)
}


}

}
