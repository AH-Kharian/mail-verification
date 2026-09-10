import secrets
import hashlib

def generate_verification_token():
    raw_token=secrets.token_urlsafe(32)
    return raw_token


import os
import resend


resend.api_key = os.environ["RESEND_API_KEY"]


def send_verification_email(user_email, verification_url):

    html = """<!--
* This email was built using Tabular.
* For more information, visit https://tabular.email
-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
<head>
<title></title>
<meta charset="UTF-8" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<!--[if !mso]><!---->
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<!--<![endif]-->
<meta name="x-apple-disable-message-reformatting" content="" />
<meta content="target-densitydpi=device-dpi" name="viewport" />
<meta content="true" name="HandheldFriendly" />
<meta content="width=device-width" name="viewport" />
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no" />
<style type="text/css">
table {
border-collapse: separate;
table-layout: fixed;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt
}
table td {
border-collapse: collapse
}
.ExternalClass {
width: 100%
}
.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {
line-height: 100%
}
body, a, li, p, h1, h2, h3 {
-ms-text-size-adjust: 100%;
-webkit-text-size-adjust: 100%;
}
html {
-webkit-text-size-adjust: none !important
}
body {
min-width: 100%;
Margin: 0px;
padding: 0px;
}
body, #innerTable {
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale
}
#innerTable img+div {
display: none;
display: none !important
}
img {
Margin: 0;
padding: 0;
-ms-interpolation-mode: bicubic
}
h1, h2, h3, p, a {
overflow-wrap: normal;
white-space: normal;
word-break: break-word
}
a {
text-decoration: none
}
h1, h2, h3, p {
min-width: 100%!important;
width: 100%!important;
max-width: 100%!important;
display: inline-block!important;
border: 0;
padding: 0;
margin: 0
}
a[x-apple-data-detectors] {
color: inherit !important;
text-decoration: none !important;
font-size: inherit !important;
font-family: inherit !important;
font-weight: inherit !important;
line-height: inherit !important
}
u + #body a {
color: inherit;
text-decoration: none;
font-size: inherit;
font-family: inherit;
font-weight: inherit;
line-height: inherit;
}
a[href^="mailto"],
a[href^="tel"],
a[href^="sms"] {
color: inherit;
text-decoration: none
}
</style>
<style type="text/css">
@media (max-width: 480px) {
.hm { display: none!important }
}
</style>
<style type="text/css">
@media (max-width: 480px) {
.t64{padding:0 0 22px!important}.t48,.t60,.t78,.t9{text-align:left!important}.t47,.t59,.t77,.t8{vertical-align:top!important;width:600px!important}.t6{border-top-left-radius:0!important;border-top-right-radius:0!important;padding:20px 30px!important}.t45{border-bottom-right-radius:0!important;border-bottom-left-radius:0!important;padding:30px!important}.t87{mso-line-height-alt:20px!important;line-height:20px!important}.t3{width:44px!important}
}
</style>
<!--[if !mso]><!---->
<link href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@500;800&amp;display=swap" rel="stylesheet" type="text/css" />
<!--<![endif]-->
<!--[if mso]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>
<body id="body" class="t90" style="min-width:100%;Margin:0px;padding:0px;background-color:#E0E0E0;"><div class="t89" style="background-color:#E0E0E0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td class="t88" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#E0E0E0;" valign="top" align="center">
<!--[if mso]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
<v:fill color="#E0E0E0"/>
</v:background>
<![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" id="innerTable"><tr><td class="t68" align="center">
<table class="t67" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="566" class="t66" style="width:566px;">
<table class="t65" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t64" style="padding:50px 10px 31px 10px;"><div class="t63" style="width:100%;text-align:left;"><div class="t62" style="display:inline-block;"><table class="t61" role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top">
<tr class="t60"><td></td><td class="t59" width="546" valign="top">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t58" style="width:100%;"><tr><td class="t57" style="background-color:transparent;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td class="t17" align="center">
<table class="t16" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="546" class="t15" style="width:600px;">
<table class="t14" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t13"><div class="t12" style="width:100%;text-align:left;"><div class="t11" style="display:inline-block;"><table class="t10" role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top">
<tr class="t9"><td></td><td class="t8" width="546" valign="top">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t7" style="width:100%;"><tr><td class="t6" style="overflow:hidden;background-color:#586CE0;padding:49px 50px 42px 50px;border-radius:18px 18px 0 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td class="t5" align="left">
<table class="t4" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr><td width="85" class="t3" style="width:85px;">
<table class="t2" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t1"><div style="font-size:0px;"><img class="t0" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="85" height="85" alt="" src="https://2fd7855b-f042-4f5f-b6df-4e7c47fbd427.b-cdn.net/e/ecd86dab-5de7-4b5b-b634-68d62bf1dea8/a97f848e-1e8e-43e4-9445-70f6896d6121.png"/></div></td></tr></table>
</td></tr></table>
</td></tr></table></td></tr></table>
</td>
<td></td></tr>
</table></div></div></td></tr></table>
</td></tr></table>
</td></tr><tr><td class="t56" align="center">
<table class="t55" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="546" class="t54" style="width:600px;">
<table class="t53" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t52"><div class="t51" style="width:100%;text-align:left;"><div class="t50" style="display:inline-block;"><table class="t49" role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top">
<tr class="t48"><td></td><td class="t47" width="546" valign="top">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t46" style="width:100%;"><tr><td class="t45" style="overflow:hidden;background-color:#F8F8F8;padding:40px 50px 40px 50px;border-radius:0 0 18px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td class="t23" align="center">
<table class="t22" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="381" class="t21" style="width:381px;">
<table class="t20" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t19"><h1 class="t18" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:41px;font-weight:800;font-style:normal;font-size:30px;text-decoration:none;text-transform:none;letter-spacing:-1.56px;direction:ltr;color:#191919;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Verify your Email<br/></h1></td></tr></table>
</td></tr></table>
</td></tr><tr><td><div class="t24" style="mso-line-height-rule:exactly;mso-line-height-alt:25px;line-height:25px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td class="t30" align="left">
<table class="t29" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr><td width="446" class="t28" style="width:563px;">
<table class="t27" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t26"><p class="t25" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">We received your interest in partnering with the Hub.Tap the button below to verify your email and proceed further.</p></td></tr></table>
</td></tr></table>
</td></tr><tr><td><div class="t31" style="mso-line-height-rule:exactly;mso-line-height-alt:15px;line-height:15px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td class="t37" align="left">
<table class="t36" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr><td width="234" class="t35" style="width:234px;">
<table class="t34" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t33" style="overflow:hidden;background-color:#586CE0;text-align:center;line-height:44px;mso-line-height-rule:exactly;mso-text-raise:10px;padding:10px 30px 10px 30px;border-radius:40px 40px 40px 40px;"><a class="t32" href="{{VERIFICATION_URL}}" style="display:block;margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:44px;font-weight:800;font-style:normal;font-size:12px;text-decoration:none;text-transform:uppercase;letter-spacing:2.4px;direction:ltr;color:#FFFFFF;text-align:center;mso-line-height-rule:exactly;mso-text-raise:10px;" target="_blank">Verify my Email</a></td></tr></table>
</td></tr></table>
</td></tr><tr><td><div class="t38" style="mso-line-height-rule:exactly;mso-line-height-alt:15px;line-height:15px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td class="t44" align="left">
<table class="t43" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr><td width="446" class="t42" style="width:563px;">
<table class="t41" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t40"><p class="t39" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;letter-spacing:-0.56px;direction:ltr;color:#333333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px;">This verification link will expire in 30 minutes.If you did not submit a partner application, you can safely ignore this email.</p></td></tr></table>
</td></tr></table>
</td></tr></table></td></tr></table>
</td>
<td></td></tr>
</table></div></div></td></tr></table>
</td></tr></table>
</td></tr></table></td></tr></table>
</td>
<td></td></tr>
</table></div></div></td></tr></table>
</td></tr></table>
</td></tr><tr><td class="t86" align="center">
<table class="t85" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="600" class="t84" style="width:600px;">
<table class="t83" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t82"><div class="t81" style="width:100%;text-align:left;"><div class="t80" style="display:inline-block;"><table class="t79" role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top">
<tr class="t78"><td></td><td class="t77" width="600" valign="top">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t76" style="width:100%;"><tr><td class="t75" style="padding:0 50px 0 50px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td class="t74" align="center">
<table class="t73" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="500" class="t72" style="width:600px;">
<table class="t71" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t70"><p class="t69" style="margin:0;Margin:0;font-family:Albert Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;text-transform:none;direction:ltr;color:#888888;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">© 2026 AI Hub Kharian All Rights Reserved<br/></p></td></tr></table>
</td></tr></table>
</td></tr></table></td></tr></table>
</td>
<td></td></tr>
</table></div></div></td></tr></table>
</td></tr></table>
</td></tr><tr><td><div class="t87" style="mso-line-height-rule:exactly;mso-line-height-alt:50px;line-height:50px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr></table></td></tr></table></div>
<!--[if !mso]><!---->
<div itemscope itemtype="http://schema.org/EmailMessage"><meta itemprop="subjectLine" content="Verify your Email" /></div>
<!--<![endif]-->
<div class="gmail-fix" style="display: none; white-space: nowrap; font: 15px courier; line-height: 0;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div>
</body>
</html>
    """
    html = html.replace("{{VERIFICATION_URL}}", verification_url)


    response = resend.Emails.send({
        "from": "AHK <no-reply@aihubkharian.com>",
        "to": [user_email],
        "subject": "Verify your email address",
        "html": html,
    })

    return response




