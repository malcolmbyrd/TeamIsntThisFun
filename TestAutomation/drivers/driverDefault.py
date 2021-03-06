if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from beets import autotag
        from beets import ui
    else:
        from ..beets import autotag
        from ..beets import ui
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from beets import autotag
    from beets import ui
else:
    from ..beets import autotag
    from ..beets import ui

#from TeamIsntThisFun.testAutomation.project.src.beets.beets import autotag
#from TeamIsntThisFun.testAutomation.project.src.beets.beets import ui
#from beets.autotag import hooks
#import beets

def driverDefaultFunc(info):
    """Calls the function specified in the test case specification file with the specified inputs, then returns the output."""
    # info[2]. component being tested
    # info[3]. method being tested
    # info[4]. test input(s) including command-line argument(s)
    #componentName = importlib.import_module(beets)

    try:
        inFuncName = info[3]
    except: 
        inFuncName = "human_bytes"
    try:
        inInputVal = info[4]
    except:
        pass

    ## If there is only one input value, call the function with one argument
    if (len(inInputVal) == 1):
        try:
            output = getattr(ui, inFuncName)(inInputVal[0])
        except TypeError as e:
            output = "TypeError"
        #except InputError:
        #    output = "InputError"
        except ValueError as e:
            output = "ValueError"
        except Exception, e:
            print(str(e))
            print(repr(e))
            output = "ErrorHere"
    ## If there are two input values, call function with two arguments
    elif (len(inInputVal) == 2):
        if (info[2] == "autotag"):
            #print(info[0] + "   rrr1")
            try:
                output = getattr(autotag.hooks, inFuncName)(inInputVal[0], inInputVal[1])
            except TypeError as e:
                output = "TypeError"
            #except InputError:
            #    output = "InputError"
            except AssertionError as e:
                output = "AssertionError"
            except Exception, e:
                print(str(e))
                print(repr(e))
                output = "Errorrr"
        elif (info[2] == "ui"):
            #print(info[0] + "   rrr2")
            try:
                #output = getattr(ui, "human_bytes")(None)

                output = getattr(ui, inFuncName)(inInputVal[0], inInputVal[1])
            except TypeError as e:
                output = "TypeError"
            #except InputError:
            #    output = "InputError"
            except AssertionError as e:
                output = "AssertionError"
            except Exception, e:
                print(str(e))
                print(repr(e))
                output = "Errorrr2"
    else:
        output = "Some Error"

    return output
