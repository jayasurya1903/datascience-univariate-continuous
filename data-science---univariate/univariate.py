import pandas as pd
class univariate():
    
    def quanqual(dataset):
                quan=[]
                qual=[]

                for columnName in dataset.columns:
                    if (dataset[columnName].dtype=='O'):
                        qual.append(columnName)
                    else:
                        quan.append(columnName)
                return quan,qual
            
    def mmm_percentile (quan,dataset):
        descript=pd.DataFrame(index=['mean','median','mode','Q1:25%','Q2:50%','Q3:75%','Q4:100%'],columns=quan)
        for column in quan:
            descript [column]['mean']=dataset[column].mean()
            descript [column]['median']=dataset[column].median()
            descript [column]['mode']=dataset[column].mode()[0]
            descript [column]['Q1:25%']=dataset.describe()[column]['25%']
            descript [column]['Q2:50%']=dataset.describe()[column]['50%']
            descript [column]['Q3:75%']=dataset.describe()[column]['75%']
            descript [column]['Q4:100%']=dataset.describe()[column]['max']
            
        return descript
    
    def iqr (quan,dataset):
        descript=pd.DataFrame(index=           ['mean','median','mode','Q1:25%','Q2:50%','Q3:75%','Q4:100%','IQR','1.5rule','lesser','greater','min','max'],columns=quan)
        for column in quan:
            descript [column]['mean']   =dataset[column].mean()
            descript [column]['median'] =dataset[column].median()
            descript [column]['mode']   =dataset[column].mode()[0]
            descript [column]['Q1:25%'] =dataset.describe()[column]['25%']
            descript [column]['Q2:50%'] =dataset.describe()[column]['50%']
            descript [column]['Q3:75%'] =dataset.describe()[column]['75%']
            descript [column]['Q4:100%']=dataset.describe()[column]['max']
            descript [column]['IQR']    =descript [column]['Q3:75%']-descript [column]['Q1:25%']
            descript [column]['1.5rule']=1.5*descript [column]['IQR']
            descript [column]['lesser'] =descript [column]['Q1:25%']-descript [column]['1.5rule']
            descript [column]['greater']=descript [column]['Q3:75%']+descript [column]['1.5rule']
            descript [column]['min']    =dataset[column].min()
            descript [column]['max']    =dataset[column].max()
        return descript 
    
   

    def findlessgreat(quan,descript_iqr):
        less=[]
        great=[]

        for column in quan:
            if(descript_iqr[column]['min']<descript_iqr [column]['lesser']):
                less.append(column)
            if(descript_iqr[column]['max']>descript_iqr [column]['greater']):
                great.append(column)
        return less,great
    
    def replace_outlier(dataset,descript_iqr,less,great):
        for column in less:
            dataset[column][dataset[column]<descript_iqr[column]['lesser']]=descript_iqr[column]['lesser']                   
        for column in great:
            dataset[column][dataset[column]>descript_iqr[column]['greater']]=descript_iqr[column]['greater'] 
        return dataset
    
    def replaced_data(quan,dataset):
        descript=pd.DataFrame(index=['mean','median','mode','Q1:25%','Q2:50%','Q3:75%','Q4:100%','IQR','1.5rule','lesser','greater','min','max','skewness','kurtosis'],columns=quan)
        for column in quan:
            descript [column]['mean']   =dataset[column].mean()
            descript [column]['median'] =dataset[column].median()
            descript [column]['mode']   =dataset[column].mode()[0]
            descript [column]['Q1:25%'] =dataset.describe()[column]['25%']
            descript [column]['Q2:50%'] =dataset.describe()[column]['50%']
            descript [column]['Q3:75%'] =dataset.describe()[column]['75%']
            descript [column]['Q4:100%']=dataset.describe()[column]['max']
            descript [column]['IQR']    =descript [column]['Q3:75%']-descript [column]['Q1:25%']
            descript [column]['1.5rule']=1.5*descript [column]['IQR']
            descript [column]['lesser'] =descript [column]['Q1:25%']-descript [column]['1.5rule']
            descript [column]['greater']=descript [column]['Q3:75%']+descript [column]['1.5rule']
            descript [column]['min']    =dataset[column].min()
            descript [column]['max']    =dataset[column].max()
            descript[column]['skewness']=dataset[column].skew()
            descript[column]['kurtosis']=dataset[column].kurtosis()
            
        return descript
    
    
    def check_less_great(replaced_newdata,quan):
        less=[]
        great=[]

        for column in quan:
            if(replaced_newdata[column]['min']<replaced_newdata[column]['lesser']):
                less.append(column)
            if(replaced_newdata[column]['max']>replaced_newdata [column]['greater']):
                great.append(column)
        return less,great
    
    
    def freqtable(columnname,dataset):
        freqtab=pd.DataFrame(columns=['uniquevalue','frequency','relativefrequency','cumulativefrequency'])
        freqtab['uniquevalue']=dataset['ssc_p'].value_counts().index
        freqtab['frequency']=dataset['ssc_p'].value_counts().values
        freqtab['relativefrequency']=freqtab['frequency']/103
        freqtab['cumulativefrequency']=freqtab['relativefrequency'].cumsum()
        return freqtab

    
    
    
    
    
    
    
    
    