[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Build Status](https://travis-ci.org/hilarak/odoo_community_addons.svg?branch=10.0)](https://travis-ci.org/hilarak/odoo_community_addons)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8717dc7e3eae4124971361b6a67be824)](https://www.codacy.com/app/hilarak/odoo_community_addons?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hilarak/odoo_community_addons&amp;utm_campaign=Badge_Grade)
# HR Dasboard

Hr Dashboard is an odoo addon for HRMS. Dashboard which displays a lot of human resource related details scattered in different menus in a single container. Here the details and the count of data need approval are shown. So its access is limited to Human resource manager or officers.

  - Approval Menus
  - Leave Details
  - Attendace Details
  - Recruitment deatils
  - Timesheets
  - Employee Expeses
  - Payroll Month wise analysis
  - Employee wise attendance analysis
  - Total Worked Hours of each employees
  - Employee details as a Table
  - Export to pdf, xls, csv and direct print

# Features!

  - Export Employee details as pdf, xls, csv
  - Export Charts to pdf
  - Approval Menus on single screen



> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.


### Tech

HR Dashboard uses

* [PYTHON](https://www.python.org/) - Models
* [XML](https://www.w3.org/XML/) - Views
* [HTML](https://www.w3.org/html/) - UI
* [Twitter Bootstrap](http://getbootstrap.com/2.3.2/) - UI
* [backbone.js](http://backbonejs.org/) - Views
* [jQuery](https://jquery.com/)

### Installation

Install the odoo10 and HRMS modules defined in manifest. After installation you can see a new menu 'HR Dashboard' for users who are officer/manager in Human Resource Odoo.

### Note
On windows servers, There is a common issue related with odoo, from this link [https://github.com/odoo/odoo/issues/14581?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging%3BO18X%2FE98SVKdiEiTCbko2Q%3D%3D](https://github.com/odoo/odoo/issues/14581?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging%3BO18X%2FE98SVKdiEiTCbko2Q%3D%3D) 

solution:-
Install this addon [Fix Error Blank Page](https://apps.odoo.com/apps/modules/10.0/web_fix_blank_page/) or do this script
```
UPDATE ir_attachment 
SET mimetype = 'text/javascript' 
WHERE mimetype ='text/plain' 
and datas_fname like '%.js';
```

### Todos

 - ADD more employee datas
 - More Comparison charts

License
----
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
