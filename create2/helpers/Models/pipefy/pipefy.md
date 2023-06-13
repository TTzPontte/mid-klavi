
the pipefy api allows us to perform the following query

{
  table_records(table_id: 303051866){
    edges{
      node{
        id
      }
    }
  }
}

TableRecordSearch
Records search's inputs

INPUT FIELDS : OBJECT	DESCRIPTION
assignee_ids: [ID]	The assignee ID
ignore_ids: [ID]	The records ID to be ignored
label_ids: [ID]	The label ID
orderDirection: String	The sort direction Valid options: - asc - desc
orderField: String	The field used to sort results
title: String	The record title
include_done: Boolean	Shows or not done records

allCards
Fetches all pipe cards based on arguments

QUERY : RETURN OBJECT
allCards: CardConnection
ARGUMENT : OBJECT	DESCRIPTION
first: Int	Returns the first _n_ elements from the list.
after: String	Returns the elements in the list that come after the specified cursor.
last: Int	Returns the last _n_ elements from the list.
before: String	Returns the elements in the list that come before the specified cursor.
pipeId: ID!	Required. The pipe ID
filter: AdvancedSearch	Search filter

CardConnection
The connection type for Card.

FIELD : OBJECT	DESCRIPTION
edges: [CardEdge]	A list of edges.
pageInfo: PageInfo	Information to aid in pagination.

CardEdge
An edge in a connection.

FIELD : OBJECT	DESCRIPTION
cursor: String	A cursor for use in pagination.
node: Card	The item at the end of the edge.

Card
List of card information

FIELD : OBJECT	DESCRIPTION
age: Int	The seconds since the card was created
assignees: [User]	Information about the assigned users
attachments: [Attachment]	Information about the attached files
attachments_count: Int	The card total attachments
cardAssignees: [CardAssignee]	Information about the card's assignees
checklist_items_checked_count: Int	The card total checked items
checklist_items_count: Int	The card total checklist items
child_relations: [CardRelationship]	Information about the child pipe connections
comments: [Comment]	Information about the card comments
comments_count: Int	The card total comments
createdAt: DateTime	When the card was created
createdBy: User	Information about the card creator
creatorEmail: String	The email the card creator
currentLateness: cardLateness	Information about the card lateness
current_phase: Phase	Information about the card current phase
current_phase_age: Int	The seconds since the card entered current phase
done: Boolean	Whether the card is done
due_date: DateTime	The card due date
emailMessagingAddress: String	The card email address
expiration: CardExpiration	Information about the card expiration
expired: Boolean	Whether the card is expired
fields: [CardField]	Information about the card fields
finished_at: DateTime	When the card was finished
id: ID	The card ID
inboxEmailsRead: Boolean	Information about any inbox email read status
inbox_emails: [InboxEmail]	Information about the card emails
labels: [Label]	Information about the card labels
late: Boolean	Whether the card is late
parent_relations: [CardRelationship]	Information about the parent pipe connections
path: String	The card path
phases_history: [PhaseDetail]	Information about the phases the card went through
pipe: Pipe	Information about the pipe
started_current_phase_at: DateTime	When the card first entered the current phase
subtitles: [CardField]	Information about the card subtitles
suid: String	The card Small Unique ID
summary: [Summary]	Information about the card summary layout
summary_attributes: [Summary]	Information about the card attributes summary layout
summary_fields: [Summary]	Information about the card custom fields summary layout
title: String	The card title
updated_at: DateTime	When the card was last updated
url: String	The card URL
uuid: String	The card Unique UUID
DEPRECATED : OBJECT	DESCRIPTION
created_at	Deprecated. When the card was created
created_by	Deprecated. Information about the card creator
repo	Deprecated. Information about the card current Repo

AdvancedSearch
Advanced search's inputs

INPUT FIELDS : OBJECT	DESCRIPTION
field: String	The field slug
operator: AdvancedSearchOperators	The search operator
value: String	The field value
AND: [AdvancedSearch]	Logical AND on all given filters
OR: [AdvancedSearch]	Logical OR on all given filters

AdvancedSearchOperators
Advanced search valid operators

ENUM VALUES : OBJECT	DESCRIPTION
equal:	Equals to
gt:	Greater than
gte:	Greater than or equal to
lt:	Less than
lte: 	Less than or equal to


table_records
Fetches a group of records based on arguments

QUERY : RETURN OBJECT
table_records: TableRecordWithCountConnection
ARGUMENT : OBJECT	DESCRIPTION
first: Int	Returns the first _n_ elements from the list.
after: String	Returns the elements in the list that come after the specified cursor.
last: Int	Returns the last _n_ elements from the list.
before: String	Returns the elements in the list that come before the specified cursor.
table_id: ID!	Required. The table ID
search: TableRecordSearch	Arguments that can be used to filter the search
