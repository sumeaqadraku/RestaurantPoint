from enums import UserRole, UserFeatures

class AuthorizationService:
    # Class responsible for providing user features based on user role
    
    def get_user_feature_by_user_role(self, user_role):
        
        #Returns the list of user features based on the user's role
        if user_role == UserRole.ADMIN:
            return [UserFeatures.EMPLOYEES, UserFeatures.DEPARTMENTS, UserFeatures.PAYROLLS, UserFeatures.ACCOUNTS, UserFeatures.HOLIDAYS, UserFeatures.SIGN_OUT]
        elif user_role == UserRole.EMPLOYEE:
            return [UserFeatures.CUSTOMERS, UserFeatures.TASK, UserFeatures.SALES, UserFeatures.CALENDAR, UserFeatures.SIGN_OUT]
        elif user_role == UserRole.INTERN:
            return [UserFeatures.CALENDAR, UserFeatures.TASK, UserFeatures.SIGN_OUT]
        elif user_role is None:
            raise RuntimeError("The provided user role " + user_role + " is not supported")
        
class UserFeatureLabelResolver:
    #Class responsible for resolving user feature labels
    
    user_feature_label_dict = None
    
    @staticmethod
    def get_user_feature_label(user_feature):
        return UserFeatureLabelResolver.__get_user_feature_label_dict().get(user_feature)
        
    
    @staticmethod
    def __get_user_feature_label_dict():
        if UserFeatureLabelResolver.user_feature_label_dict is None:
            UserFeatureLabelResolver.user_feature_label_dict = {
                UserFeatures.EMPLOYEES : "Employees",
                UserFeatures.DEPARTMENTS: "Departments",
                UserFeatures.PAYROLLS: "Payrolls",
                UserFeatures.HOLIDAYS: " Holidays",
                UserFeatures.ACCOUNTS : "Accounts",
                UserFeatures.CUSTOMERS : "Customers",
                UserFeatures.SALES: "Sales",
                UserFeatures.CALENDAR : "Calendar",
                UserFeatures.TASK : "Task",
                UserFeatures.SIGN_OUT : " Sign Out"
                
            }
            
        return UserFeatureLabelResolver.user_feature_label_dict
            
            