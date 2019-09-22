
/* SERVL LOG CLASS TEMPLATE #1 */
/* Created: 22/09/2019 by GA */

import java.util.*;

public class Log{
        private String Workplace = "";
        private String ID = "";
        private Date Checkin = null;

        Log(String Workplace, String ID, Date Checkin){
                this.Workplace = Workplace;
                this.ID = ID;
                this.Checkin = Checkin;
        }

        //Getters
        public String getWorkplace(){
                return this.Workplace;
        }

        public String getID(){
                return this.ID;
        }
        
        public Date getCheckin(){
                return this.Checkin;
        }
        // Setters & modification is not allowed at this stage
}
