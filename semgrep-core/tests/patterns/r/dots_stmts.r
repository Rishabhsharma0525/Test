foo <- function () {
    #ERROR:
    user_data <- get()
    print("do stuff")
    foobar()
    eval(user_data)
}
