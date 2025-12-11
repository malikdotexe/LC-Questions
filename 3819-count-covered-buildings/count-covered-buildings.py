class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xdict = {} # xindex : [miny,maxy]
        ydict = {}
        count = 0
        #Updating dict with buildings data
        for [x,y] in buildings:
            #if its not initialized already
            if x not in xdict:
                xdict[x] = [y,y]
            #Else we update miny and maxy
            else:
                if xdict[x][0] > y:
                    xdict[x][0]= y
                if xdict[x][1]<y:
                    xdict[x][1]=y
            #Same for y dict
            if y not in ydict:
                ydict[y] = [x,x]
            else:
                if ydict[y][0] > x:
                    ydict[y][0]= x
                if ydict[y][1]<x:
                    ydict[y][1]=x
        #Counting convered building
        for [x,y] in buildings:
            minx = ydict[y][0]
            maxx = ydict[y][1]
            miny = xdict[x][0]
            maxy = xdict[x][1]
   
            if minx<x<maxx and miny<y<maxy:
                count+=1
        return count

