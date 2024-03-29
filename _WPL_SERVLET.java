
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;
import java.text.SimpleDateFormat;  
import java.util.*;  


@WebServlet(urlPatterns = {"/_wpl_"})
public class Theatre extends HttpServlet {
        LinkedList<Log> logs = new LinkedList<Log>();

        //Run on page load
        public void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
                
                PrintWriter out = res.getWriter();
                res.setContentType("application/json");
                res.setCharacterEncoding("UTF-8");
                

                String RAW_WORKPLACE = req.getParameter("Workplace");
                String RAW_ID = req.getParameter("ID");
                Date date = new Date();
                
                if(RAW_WORKPLACE == null && RAW_ID == null){
                        Log Temp = new Log(RAW_WORKPLACE, RAW_ID, date);
                        logs.add(Temp);
                }
                out.print("{ \"workplace\":\"" + RAW_WORKPLACE + "\", \"ID\":\"" + RAW_ID +"\", \"Time\":\"" + date + "\"}");
                
                out.flush();

                
        }

        //sends the post request
        protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        }
        
}
