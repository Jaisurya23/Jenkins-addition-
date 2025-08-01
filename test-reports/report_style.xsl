<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
        <head>
            <title>Test Report</title>
            <style>
                table { border-collapse: collapse; width: 80%; margin: auto; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2 align="center">Unit Test Report</h2>
            <table>
                <tr>
                    <th>Test Case</th>
                    <th>Status</th>
                    <th>Time</th>
                </tr>
                <xsl:for-each select="testsuites/testsuite/testcase">
                    <tr>
                        <td><xsl:value-of select="@name"/></td>
                        <td>
                            <xsl:choose>
                                <xsl:when test="failure">❌ Failed</xsl:when>
                                <xsl:otherwise>✅ Passed</xsl:otherwise>
                            </xsl:choose>
                        </td>
                        <td><xsl:value-of select="@time"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
