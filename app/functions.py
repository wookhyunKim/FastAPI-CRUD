from db import Databases

class CRUD(Databases):
    # def insertDB(self,schema,table,colum,data):
    #     sql = " INSERT INTO {schema}.{table} ({colum}) VALUES ('{data}') ;".format(schema=schema,table=table,colum=colum,data=data)
    #     try:
    #         self.cursor.execute(sql)
    #         self.db.commit()
    #         rs = True
    #     except Exception as e :
    #         print(" insert DB err ",e) 
    #         rs = False
    #     return rs    
    
    def insertDB(self, table, column, data):
        sql = f"INSERT INTO {table} ({column}) VALUES (%s, %s)"
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
            rs = True
        except Exception as e:
            print("insert DB err", e)
            rs = False
        return rs
    

    def readDB_All(self,table,column):
        sql = f" SELECT {column} from {table}"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            rs = True
        except Exception as e :
            result = (" read DB err",e)
            rs =False
        return rs,result
    


    def readDB_One(self,table,column,fid):
        sql = f" SELECT {column} from {table} where fid = {fid}"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            rs = True
        except Exception as e :
            result = (" read DB err",e)
            rs =False
        return rs,result

    def updateDB(self,table,fname,fprice,fid):
        sql  = f"update {table} set fname='{fname}', fprice={fprice} where fid = {fid}"
        try :
            self.cursor.execute(sql)
            self.db.commit()
            rs = True
        except Exception as e :
            print(" update DB err",e)
            rs = False 
        return rs

    def deleteDB(self,table,fid):
        sql = f" delete from {table} where fid = {fid} ;"
        try :
            self.cursor.execute(sql)
            self.db.commit()
            rs = True
        except Exception as e:
            print( "delete DB err", e)
            rs = False
        return rs
