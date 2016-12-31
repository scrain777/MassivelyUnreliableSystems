Public Class SimErr

    Private mLog As System.IO.StreamWriter
    Private mIntErrors As Integer
    Private mIntFixed As Integer

    ' Initialize
    '
    ' Input: The name of a file in which to log the errors and fixes.
    '
    Sub New(filename As String)
        Randomize()
        mLog = My.Computer.FileSystem.OpenTextFileWriter(filename, True)
    End Sub

    ' Simulate an error condition.
    '
    ' Input: the number of lines in the calling function. More lines indicates
    '        higher complexity so we simulate more errors.
    '
    ' Return: 1 indicates that an error is to be simulated. 0 indicates no error.
    '
    Public Function SimError(func As String, lines As Integer) As Integer
        ' Do not want any cheating...
        func = func.Replace(vbLf, " "c)

        If (lines < 1 Or Rnd() < lines * lines * 0.000001) Then
            mIntErrors = mIntErrors + 1
            mLog.Write("Hit error ")
            mLog.Write(mIntErrors)
            mLog.WriteLine(" in function " + func + ".")
            Return 1
        End If

        Return 0
    End Function

    ' Record a correction from a simulated error.
    '
    ' Input: message indicating how the error was handled.
    '
    Public Sub SimFix(msg As String)
        ' Do not want any cheating...
        msg = msg.Replace(vbLf, " ")
        mIntFixed = mIntFixed + 1
        mLog.Write("Error fix [")
        mLog.Write(mIntFixed)
        mLog.Write("/")
        mLog.Write(mIntErrors)
        mLog.WriteLine("]: " + msg)
    End Sub

    ' Print a final summary and close the log.
    '
    Public Sub SimDone()
        mLog.WriteLine()
        mLog.WriteLine()
        mLog.Write("Summary: Fixed ")
        mLog.Write(mIntFixed)
        mLog.Write("/")
        mLog.WriteLine(mIntErrors)
        mLog.Close()
    End Sub
End Class
