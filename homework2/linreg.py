import numpy as np

def linreg(df, target_column):
    global log
    
    try:
        # prepare X,Y
        #
        # remove NaN values
        np.set_printoptions(suppress=True)
        df = df.dropna()
        # get target row (= target_column)
        dy = np.array(df[target_column].values)
        dy = np.reshape(dy, (len(dy), 1))
        # get covariates (<> target_column)
        dx = np.array(df.drop(target_column, axis=1).values)
        # create new matrix with target as first column
        dc = np.concatenate((dy, dx), axis=1).astype(np.float64)
        # center matrix
        dc = dc - dc.mean(axis=0)
        # get target as NumPy (colum vector)
        Y = dc[:,0]
        Y = np.reshape(Y, (-1, 1))
        # get covariates as NumPy
        X = np.delete(dc, 0, 1)
        # get estimate beta
        #
        # add 1 to matrix
        XA = np.concatenate((np.ones((len(Y),1)), X), axis = 1)
        # XT = transfer-matrix form X
        XT = XA.transpose()
        # XTX = XT * X
        XTX = np.dot(XT,XA)
        # XTXI = inverse matrix from XTX
        XTXI = np.linalg.inv(XTX)

        # the 3 matrices multiplied
        beta = XTXI @ XT @ Y    
        # get standard error
        #
        # YH = Y hat
        YH = XA @ beta
        # E = sigma
        # E = sigma
        E = Y - YH
        # E = sigma suqared
        E_SQRT = (E.T @ E) / (len(Y)- len(X[1,:]) -1)
        # VAR = covariance matrix
        VAR = E_SQRT * np.linalg.inv(np.dot(XT,XA))
        #c = colum count from df
        c = X.shape[1]+Y.shape[1] 
        stderror = np.array([np.sqrt(VAR[i,i]) for i in range(c)])
        #get t-statistic
        tstat = np.array([beta[i]/np.sqrt(VAR[i,i]) for i in range(c)])
        return beta[:,0], stderror, tstat[:,0]
    except RuntimeError:
        log = "RuntimeError"
        return [0], [0], [0]
    except TypeError:
        log = "TypeError"
        return [0], [0], [0]
    except NameError:
        log = "NameError"
        return [0], [0], [0]
    except Warning:
        log = "Warning"
        return [0], [0], [0]
    except FloatingPointError:
        log = "Division by zero"
        return [0], [0], [0]
    except ZeroDivisionError:
        log = "Division by zero"
        return [0], [0], [0]
    except:
        log = "Something else went wrong"
        return [0], [0], [0]