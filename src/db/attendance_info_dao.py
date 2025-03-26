from src.db.database import DataBase

class AttendanceInfoDAO:
    def __init__(self, db: DataBase):
        self.db = db

    def get_daily_attendance_num_by_course(self, course_name):
        query = """
            SELECT COUNT(*)
        FROM(
        SELECT total.date, total.count1, attend.count2, attend.count2 / total.count1
        FROM 
            (SELECT date, COUNT(*) AS count1
            FROM attendance_info
            WHERE course_name=%s
            GROUP BY date
            ) AS total
        JOIN
            (SELECT date, COUNT(*) AS count2
            FROM attendance_info
            WHERE course_name = %s AND is_attendance = TRUE
            GROUP BY date) as attend
        ON total.date = attend.date
        GROUP BY total.date) AS res;"""

        params = [course_name, course_name]
        res = self.db.fetchall(query, params)
        return res[0][0]    # 返回的是这个课程总共签到了多少天
    
    
    def get_daily_attendance_info_by_course(self, course_name):
        query = """
            SELECT total.date, total.count1, attend.count2, attend.count2 / total.count1
        FROM 
            (SELECT date, COUNT(*) AS count1
            FROM attendance_info
            WHERE course_name=%s
            GROUP BY date
            ) AS total
        JOIN
            (SELECT date, COUNT(*) AS count2
            FROM attendance_info
            WHERE course_name = %s AND is_attendance = TRUE
            GROUP BY date) as attend
        ON total.date = attend.date
        GROUP BY total.date;"""

        params = [course_name, course_name]
        res = self.db.fetchall(query, params)
        return res

    
    
        

