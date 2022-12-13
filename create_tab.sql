USE [CInfo]
GO

/****** Object:  Table [dbo].[polls]    Script Date: 13.12.2022 14:46:18 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[polls](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nchar](10) NOT NULL,
	[descr] [ntext] NULL,
	[is_act] [int] NOT NULL,
	[is_del] [int] NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

ALTER TABLE [dbo].[polls] ADD  CONSTRAINT [DF_poll2_is_act]  DEFAULT ((0)) FOR [is_act]
GO

ALTER TABLE [dbo].[polls] ADD  CONSTRAINT [DF_poll2_is_del]  DEFAULT ((0)) FOR [is_del]
GO


